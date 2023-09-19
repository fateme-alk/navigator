# Navigator
Navigator is a custom mapping and navigation app which finds the best route to a specific destination.
![Capture](https://github.com/fateme-alk/navigator/assets/136516189/d578316e-3353-458b-bf12-281ff28741d1)

## Installation
1. Clone the repository:
   * Open a terminal or command prompt
   * Navigate to the directory where you want to clone the repository.
   * Run the following command:
     
     ```
     git clone https://github.com/fateme-alk/navigator.git
     ``` 
2. Create a conda environment from YAML file
   * Direct the terminal where you cloned the repository
   * Conda will read the YAML file and set up a new environment with the dependencies specified
   * Run the following command:
     
     ```
     conda env create --name nav --file=environment.yml
     ```
   * This process may take a few minutes, as Conda will download and install the necessary packages
   * Once the environment is created, you can activate it by running the following command
     
     ```
     conda activate nav
     ```
  3. Run the backend server with Flask
     * Run the following command:
       
       ```
       flask --app main run
       ```
     * You should see output similar to the below picture that means the server is up and running on your local machine
       ![flaskserver](https://github.com/fateme-alk/navigator/assets/136516189/c17c4b71-9424-49ca-a6cc-1cf55d8412cc)
  4. Launch the frontend app using Live Server in VS Code
     * Ensure the Live Server extension is installed in your Visual Studio Code (VS Code) editor. If not, you can easily install it from the Visual Studio Code marketplace.
     * Right-click on map.html file, and select the "Open with Live Server" option from the context menu.
     * Now you can interact with the app in the browser window provided by the Live Server extension
