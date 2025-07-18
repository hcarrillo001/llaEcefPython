import pytest

from EcefCoordinate import EcefCoordinate
from EcefVelocity import EcefVelocity
from LLaCoordinate import LLaCoordinate
from Main import covert_lla_to_ecef, calculate_ecef_velocities, calculate_interpolating_velocities


#test


def test_convert_lla_to_ecef():
    epochTime = 1532332859.04
    a = 6378137
    lat = 34.0522
    lon = -118.2437
    alt = 100.00

    llacoordinate = LLaCoordinate(epochTime,lat,lon,alt)
    llacoordinates = [llacoordinate]

    ecefcoodinates = covert_lla_to_ecef(llacoordinates)

    assert (ecefcoodinates[0].get_x()) == -2503396.5198597223
    assert(ecefcoodinates[0].get_y()) == -4660276.422746513
    assert(ecefcoodinates[0].get_z()) == 3551301.35408728


    #Another coordinate
    lat = 0
    lon = 0
    alt = 0

    llacoordinate = LLaCoordinate(epochTime, lat, lon, alt)
    llacoordinates[0] = llacoordinate
    ecefcoodinates = covert_lla_to_ecef(llacoordinates)

    assert (ecefcoodinates[0].get_x()) == 6378137.0
    assert (ecefcoodinates[0].get_y()) == 0
    assert (ecefcoodinates[0].get_z()) == 0


    #Edge case scenario 90 north pole
    lat = 90
    lon = 0
    alt = 0

    llacoordinate = LLaCoordinate(epochTime, lat, lon, alt)
    llacoordinates = [llacoordinate]
    ecefcoodinates = covert_lla_to_ecef(llacoordinates)

    assert (ecefcoodinates[0].get_x()) == pytest.approx(3.918620924814471e-10)
    assert (ecefcoodinates[0].get_y()) == 0
    assert (ecefcoodinates[0].get_z()) == 6356752.31424518

    #Edge Case at 90 lat (South pole)
    lat = -90
    lon = 0
    alt = 0

    llacoordinate = LLaCoordinate(epochTime, lat, lon, alt)
    llacoordinates = [llacoordinate]
    ecefcoodinates = covert_lla_to_ecef(llacoordinates)

    assert (ecefcoodinates[0].get_x()) == pytest.approx(3.918620924814471e-10)
    assert (ecefcoodinates[0].get_y()) == 0
    assert (ecefcoodinates[0].get_z()) == -6356752.31424518

    # Longitude edge cases + / - 180
    lat = 0
    lon = 180
    alt = 0

    llacoordinate = LLaCoordinate(epochTime, lat, lon, alt)
    llacoordinates = [llacoordinate]
    ecefcoodinates = covert_lla_to_ecef(llacoordinates)

    assert (ecefcoodinates[0].get_x()) == -6378137.0
    assert (ecefcoodinates[0].get_y()) == pytest.approx(7.810965061573302e-10)
    assert (ecefcoodinates[0].get_z()) == 0

    lat = 0
    lon = -180
    alt = 0

    llacoordinate = LLaCoordinate(epochTime, lat, lon, alt)
    llacoordinates = [llacoordinate]
    ecefcoodinates = covert_lla_to_ecef(llacoordinates)

    assert (ecefcoodinates[0].get_x()) == -6378137.0
    assert (ecefcoodinates[0].get_y()) == pytest.approx(-7.810965061573302e-10)
    assert (ecefcoodinates[0].get_z()) == 0

    #Test altitude
    lat = 0
    lon = 0
    alt = 100

    llacoordinate = LLaCoordinate(epochTime, lat, lon, alt)
    llacoordinates = [llacoordinate]
    ecefcoodinates = covert_lla_to_ecef(llacoordinates)

    assert ecefcoodinates[0].get_x() > a

def test_invalid_value_convert_lla_to_ecef():
    epochTime = 1532332859.04
    # test invalid value
    lat = 100;
    lon = 0;
    alt = 0;

    llacoordinate = LLaCoordinate(epochTime, lat, lon, alt)
    llacoordinates = [llacoordinate]

    with pytest.raises(ValueError) as excinfo:
        covert_lla_to_ecef(llacoordinates)
    assert excinfo.type is ValueError



def test_calculate_ecef_velocities():
    # Basic example(1 second differnce)
    epochtime1 = 1532332859.04
    epochtime2 = 1532332860.04
    ecefCoordinate1 = EcefCoordinate(epochtime1, 1000.00, 2000.00, 3000)
    ecefCoordinate2 = EcefCoordinate(epochtime2, 1000.00, 4000.00, 6000)

    ecefCoordinates = [ecefCoordinate1,ecefCoordinate2]

    ecefvelocitylist = calculate_ecef_velocities(ecefCoordinates)

    assert (ecefvelocitylist[1].get_vx()) == 0
    assert (ecefvelocitylist[1].get_vy()) == 2000
    assert (ecefvelocitylist[1].get_vz()) == 3000

    #using bad data
    epochTime1 = 1532332859.04
    epochTime2 = 1532332859.04
    ecefcoordinate1 = EcefCoordinate(epochTime1, 1000.00, 2000.00, 3000)
    ecefcoordinate2 = EcefCoordinate(epochTime2, 1000.00, 4000.00, 6000)
    ecefCoordinates = []
    ecefCoordinates = [ecefcoordinate1, ecefcoordinate2]

    with pytest.raises(ValueError) as excinfo:
        calculate_ecef_velocities(ecefCoordinates)
    assert excinfo.type is ValueError


def test_calculating_interpolate_times():
    epochTime = 1532332862


    #x1,y1,y1,x2,y2,y2, delta_time will be set to 0s, purpose is just to calculate the velocities
    ecefvelocity0 = EcefVelocity(0, 0, 0, 0,0,0,0,0,0,0,1532332859)
    ecefvelocity1 = EcefVelocity(1000.00, 0, 0, 0,0,0,0,0,0,0,1532332861)
    ecefvelocity2 = EcefVelocity(1000.00, 1000.00, 0,0,0,0,0,0,0,0, 1532332863)
    ecefvelocity3 = EcefVelocity(1000.00, 1000.00, 0,0,0,0,0,0,0,1000.00, 1532332865)

    ecefvelocities = [ecefvelocity0,ecefvelocity1,ecefvelocity2,ecefvelocity3]
    ecefvelocity = calculate_interpolating_velocities(ecefvelocities, epochTime)

    assert ecefvelocity.get_vx() == 1000.0
    assert ecefvelocity.get_vy() == 500.00
    assert ecefvelocity.get_vz() == 0.00

    #Vx: 1000.0        (no movement in this direction so remains 1000.00)
    #Vy: 500.0         (This is expected which is half the distance)
    #Vz: 0.0           (no movement in this direction)
