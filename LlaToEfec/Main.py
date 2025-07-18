import math
import sys
import simplekml

from EcefCoordinate import EcefCoordinate
from EcefVelocity import EcefVelocity
from LLaCoordinate import LLaCoordinate

# Constants
a = 6378137.0                  # semi-major axis (equatorial distance)
b = 6356752.31424518           # semi-minor axis (polar radius)


# First eccentricity (e1)
e1 = math.sqrt((a**2 - b**2) / a**2)
# Second eccentricity (e2)
e2 = math.sqrt((a**2 - b**2) / b**2)



def main():
    file_path = "resources/data4.csv"
    #file_path = "resources/projectile_data_100_entries.csv"
    lla_coordinates_list = read_data_from_file(file_path)

    # https://docs.python.org/3/howto/sorting.html
    lla_coordinates_list.sort(key=lambda val: val._epoch_time)

    #Debug purposes
    for lla_coordinate in lla_coordinates_list:
        print("Epoch Time: ", lla_coordinate._epoch_time)
        print("Lat: ", lla_coordinate._lat_degree)
        print("Lon: ", lla_coordinate._lon_degree)
        print("Alt: ", lla_coordinate._altitude_meters)
        print("")

    #convert LLA to ECEF this passes an array of llaCoordinates
    ecef_coordinates = covert_lla_to_ecef(lla_coordinates_list)




    #Calculate EcefVelocities
    ecef_velocities = calculate_ecef_velocities(ecef_coordinates)

    # Debug print statement
    for EcefVelocity in ecef_velocities:
        print("Epoch Time: ", EcefVelocity.epochTime)
        print("Vx: ", EcefVelocity.vx)
        print("Vy: ", EcefVelocity.vy)
        print("Vz: ", EcefVelocity.vz)
        print("")

    first_lla_coordinate = lla_coordinates_list[0]
    min_epoch_time = first_lla_coordinate._epoch_time

    last_epoch_time = lla_coordinates_list[len(lla_coordinates_list)-1]
    max_epoch_time = last_epoch_time._epoch_time

    epoch_user_input_values = get_epoch_user_input(min_epoch_time, max_epoch_time)

    for epoch_time in epoch_user_input_values:
        interpolating_velocity = calculate_interpolating_velocities(ecef_velocities,epoch_time)
        print("Epoch Time: ", epoch_time)
        print("Vx: ", interpolating_velocity.vx, "meters/sec")
        print("Vy: ", interpolating_velocity.vy, "meters/sec")
        print("Vz: ", interpolating_velocity.vz, "meters/sec")
        print("")

    create_kml_file(lla_coordinates_list)



def create_kml_file(lla_coordinates_list):
    # Create an instance of Kml
    kml = simplekml.Kml(open=1)

    #convert list of coordinates to tuples
    coordinate_tuples = []
    for coordinate_object in lla_coordinates_list:
        coordinatetuple = (coordinate_object._lat_degree, coordinate_object._lon_degree,coordinate_object._altitude_meters)
        coordinate_tuples.append(coordinatetuple)


    linestring = kml.newlinestring(name="A Sloped Line")
    linestring.coords = coordinate_tuples
    linestring.altitudemode = simplekml.AltitudeMode.relativetoground
    linestring.extrude = 1

    #Adding placemarkers
    kml.newpoint(name="Starting Point", coords=[(lla_coordinates_list[0]._lat_degree, lla_coordinates_list[0]._lat_degree, lla_coordinates_list[0]._altitude_meters)])

    # Save the KML file
    kml.save("kmloutput/my_project_kml_file.kml")


#note to self, stip() removes whitespace
def read_data_from_file(file_path):
    lla_coordinates = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                next_line = line.strip()
                if not next_line:
                    continue

                data_split = next_line.split(',')

                epoch_time = float(data_split[0].strip())
                lat = float(data_split[1].strip())
                lon = float(data_split[2].strip())
                altitude = float(data_split[3].strip()) * 1000  # convert to meters

                #DEBUG print(lat, lon, altitude)

                new_lla_coordinate = LLaCoordinate(epoch_time, lat, lon, altitude)
                lla_coordinates.append(new_lla_coordinate)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError as e:
        print(f"IO error: {e}")

    return lla_coordinates


def covert_lla_to_ecef(lla_coordinatesList):
    ecefCoordinates = []
    for llaCoordinate in lla_coordinatesList:
        lat = llaCoordinate._lat_degree
        lon = llaCoordinate._lon_degree
        alt = llaCoordinate._altitude_meters
        epoch_time = llaCoordinate._epoch_time

        print("Epoch Time: ", epoch_time)
        print("Lat: ", lat)
        print("Lon: ", lon)
        print("Alt: ", alt)
        print("")


        # Validate latitude and longitude
        if lat < -90.0 or lat > 90.0:
            raise ValueError("Invalid Latitude: range is -90.0 to 90.0")

        if lon < -180.0 or lon > 180.0:
            raise ValueError("Invalid Longitude: range is -180.0 to 180.0")

        # Constants (redefine if not globally available)
        #a = 6378137.0                     # semi-major axis
        #b = 6356752.31424518              # semi-minor axis
        #e1 = math.sqrt((a**2 - b**2) / a**2)

        # Convert degrees to radians
        latRad = math.radians(lat)
        lonRad = math.radians(lon)

        # Radius of curvature in the prime vertical
        n = a / math.sqrt(1 - (e1**2) * math.sin(latRad)**2)

        # Calculate ECEF coordinates
        x = (n + alt) * math.cos(latRad) * math.cos(lonRad)
        y = (n + alt) * math.cos(latRad) * math.sin(lonRad)
        z = (((b**2) / (a**2) * n) + alt) * math.sin(latRad)

        new_efec_coordinate = EcefCoordinate(epoch_time, x, y, z)
        ecefCoordinates.append(new_efec_coordinate)


    return ecefCoordinates


def calculate_ecef_velocities(ecef_coordinates):
    # The first ECEF velocity is (0, 0, 0) — No movement before the first point
    ecef_velocities = []

    first_velocity_epochTime = ecef_coordinates[0].get_epoch_time()
    ecef_velocities.append(EcefVelocity(0, 0, 0,0,0,0,
                                        ecef_coordinates[0].get_x(), ecef_coordinates[0].get_y(),ecef_coordinates[0].get_z(),
                                        0,first_velocity_epochTime))

    #loop that uses a range from 1 to ecef_coordinates length (size)
    #Start at index 1 because the first ecef velocity will be (0,0,0) vx,vy,vz
    for i in range(1, len(ecef_coordinates)):
        lag = ecef_coordinates[i - 1]
        lead = ecef_coordinates[i]

        deltaTime = lead.get_epoch_time() - lag.get_epoch_time()
        if deltaTime <= 0:
            raise ValueError("Time difference delta t must be greater than zero")

        vx = (lead.get_x() - lag.get_x()) / deltaTime
        vy = (lead.get_y() - lag.get_y()) / deltaTime
        vz = (lead.get_z() - lag.get_z()) / deltaTime
        leadingEpochTime = lead.get_epoch_time()

        ecefVelocity = EcefVelocity(vx, vy, vz,
            lag.get_x(), lag.get_y(), lag.get_z(),
            lead.get_x(), lead.get_y(), lead.get_z(),
            deltaTime, leadingEpochTime
        )

        ecef_velocities.append(ecefVelocity)

    return ecef_velocities


def get_epoch_user_input(min_epoch_time, max_epoch_time):
    print(f"Please enter two Epoch times between {min_epoch_time} and {max_epoch_time}.")
    print("We will calculate the interpolation between them. Enter the values in order.")
    print(f"If you enter anything lower than {min_epoch_time}, your ECEF velocity will be (0,0,0).")
    print(f"If you enter anything higher than {max_epoch_time}, your ECEF velocity will be the last known velocity available.")

    try:
        epoch_time1 = float(input("Enter first Epoch time (or press -1 to end program): "))
        if epoch_time1 == -1.0:
            print("Ending program")
            sys.exit(0)

        epoch_time2 = float(input("Enter second Epoch time (or press -1 end program): "))
        if epoch_time2 == -1.0:
            print("Ending program")
            sys.exit(0)

        input_epoch_user_values = [epoch_time1, epoch_time2]
        return input_epoch_user_values

    except ValueError:
        print("Invalid input. Please enter valid numeric epoch times.")
        return None


def calculate_interpolating_velocities(ecef_velocities, epoch_time):
    if epoch_time <= ecef_velocities[0].get_epoch_time():
        return ecef_velocities[0]

    if epoch_time >= ecef_velocities[-1].get_epoch_time():
        return ecef_velocities[-1]

    # Binary search to search much quicker.
    #indexes
    low = 0
    high = len(ecef_velocities) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_time = ecef_velocities[mid].get_epoch_time()


        if mid_time == epoch_time:           #epoch time found
            return ecef_velocities[mid]
        elif mid_time < epoch_time:          #left of the right
            low = mid + 1
        else:                               #right of the left
            high = mid - 1

    # low is the first index greater than the target
    # high is the last index less than or equal to the target
    lagging_velocity = ecef_velocities[high]
    leading_velocity = ecef_velocities[low]

    # Linear interpolation
    lagging_time = lagging_velocity.get_epoch_time()
    leading_time = leading_velocity.get_epoch_time()

    slope = (epoch_time - lagging_time) / (leading_time - lagging_time)

    vx = lagging_velocity.get_vx() + slope * (leading_velocity.get_vx() - lagging_velocity.get_vx())
    vy = lagging_velocity.get_vy() + slope * (leading_velocity.get_vy() - lagging_velocity.get_vy())
    vz = lagging_velocity.get_vz() + slope * (leading_velocity.get_vz() - lagging_velocity.get_vz())

    return EcefVelocity(vx, vy, vz, epoch_time)



if __name__ == "__main__":
    main()