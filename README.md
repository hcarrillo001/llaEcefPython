## Authors 
    Hanns Carrillo 


  ### Python Trajectory Predictor with KML Visualization
      
      This Python project simulates and analyzes projectile motion using geospatial and temporal data from a CSV file. It performs coordinate transformation, interpolation, and visualization using KML files for mapping in [Google Earth](https://earth.google.com/).
      
      #### 🔧 Core Functionality:
      
      * **CSV File Input**: Parses a CSV (`data6.csv`) containing Latitude, Longitude, Altitude (LLA) and corresponding UNIX epoch timestamps.
      * **LLA to ECEF Conversion**: Converts geodetic coordinates to Earth-Centered, Earth-Fixed (ECEF) coordinates.
      * **Chronological Sorting**: Ensures all entries are time-ordered by epoch values for proper processing.
      * **ECEF Velocity Calculation**: Computes velocity vectors by numerically differentiating ECEF positions over time.
      * **User Epoch Input**:
      
        * Prompts the user to enter a custom epoch timestamp **not already in the dataset**.
        * Interpolates ECEF velocity and position for the given time.
        * Converts interpolated ECEF position back to LLA.
      
      #### 🌍 Google Earth Integration (KML Output):
      
      * **KML Generation**: The script generates a `.kml` file that can be loaded directly into [Google Earth](https://earth.google.com/).
      * **Mapped Content**:
      
        * All trajectory points are plotted using their LLA coordinates.
        * Associated ECEF coordinates and velocities are included as data overlays (e.g., in placemark descriptions or extended data).
        * The **interpolated interception point** (based on the user-provided epoch time) is clearly marked, showing where a trajectory would be intercepted or located at that exact                 moment, showing where a trajectory would be intercepted or located at that exact moment in time. in time.
      
      #### 💡 Skills Demonstrated:
      
      * Geospatial coordinate system transformations (LLA ↔ ECEF)
      * Numerical interpolation and vector computation
      * Python file I/O and structured data handling
      * KML file creation for 3D visualization
      * Integration with real-world tools like Google Earth for interactive analysis
 

## Testing 
     Testing was done using PyTest 


#### 🌍 Google Earth Integration

📄 How to Load a KML File
This guide explains how to open and view a .kml (Keyhole Markup Language) file in different tools for map visualization and analysis.

<img width="1469" height="747" alt="Screenshot 2025-07-19 at 8 25 34 PM" src="https://github.com/user-attachments/assets/7948cffd-c6b2-46cc-8330-5624a7a13778" />
<img width="1461" height="647" alt="Screenshot 2025-07-19 at 8 25 55 PM" src="https://github.com/user-attachments/assets/319fd684-36f0-4607-95e1-41eaa9868736" />


Viewing Coordinates in Google Earth
Initially, all coordinates will be hidden on the map.

    To view them:
    
        - Expand the KML layer in the left sidebar of Google Earth.
    
        - Click the checkbox next to “Show Feature” to enable the coordinate display.
    
    Once enabled:
    
        - Click on any coordinate point on the map to view detailed information, such as:
    
            - ECEF position
    
            - Velocity
    
            - Timestamp

<img width="1463" height="773" alt="Screenshot 2025-07-19 at 8 24 01 PM" src="https://github.com/user-attachments/assets/560acac1-724f-4ab9-87d0-d203658d1ef6" />

<img width="1457" height="771" alt="Screenshot 2025-07-19 at 8 24 59 PM" src="https://github.com/user-attachments/assets/e8f21260-8291-496b-ba4d-5ea7e1a81e21" />


🎯 Trajectory Interception Coordinate

<img width="1464" height="820" alt="Screenshot 2025-07-19 at 8 30 41 PM" src="https://github.com/user-attachments/assets/b7a5473d-396e-41fb-a5a4-c65a0ccb1c8d" />




