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
        * The **interpolated interception point** (based on the user-provided epoch time) is clearly marked, showing where a trajectory would be intercepted or located at that exact moment in time.
      
      #### 💡 Skills Demonstrated:
      
      * Geospatial coordinate system transformations (LLA ↔ ECEF)
      * Numerical interpolation and vector computation
      * Python file I/O and structured data handling
      * KML file creation for 3D visualization
      * Integration with real-world tools like Google Earth for interactive analysis
 

## Testing 
     Testing was done using PyTest 


* **KML Generation**
