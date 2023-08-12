# Lorenz System Animator (Python)

This repository contains a Python implementation of a Lorenz system animator. It uses the following equations to generate data for the graph:

<img src = "https://latex.codecogs.com/svg.image?\frac{dx}{dt}=\sigma(y-x)">

<img src = "https://latex.codecogs.com/svg.image?\frac{dy}{dt}=x(\rho-z)-y">

<img src = "https://latex.codecogs.com/svg.image?\frac{dz}{dt}=xy-\beta&space;z">


There is also a Lorenz graph generator for those that are interested. It is not compiled to an .exe like the animator but is capable of calculating more iterations in less time.

## Table of Contents

1. [Features](/README.md#features)
2. [Dependencies](/README.md#dependencies)
3. [Building and Running](/README.md#building-and-running)
4. [Example](/README.md#usage)
5. [Contributing](/README.md#contributing)
6. [License](/README.md#license)

## Features

- Prompts user with animation settings and information.
- Animation provides live updates with where function is at in terms of constants.
- Real-time progress bar lets the user know how many frames have been compiled during rendering.
- Upon completing the animation, it lets the user know that it is saved to the directory in which the .exe file is located.

## Dependencies

This project depends on the following libraries which are all compiled into the .exe:

- matplotlib
- tqdm
- time
- pillow
- mpl_toolkits

## Building and Running

### Windows

It is a little bit long because large files are stored using Git LFS but should work if you follow these steps:

1. Download the .zip file by pressing the green "Code" button and selecting "Download ZIP".
2. Go to your computers downloads folder and right click on the file to extract all components to a folder on your computer. 
3. Go back to this Github repository and navigate to build/animate -> animate.pkg. Press "View Raw" to download this file.
4. Once the file is downloaded, go to your computers downloads folder and right click on the file to cut it. 
6. Go to your extracted folder and paste the file into the build/animate folder. Press yes when prompted to replace the file.
7. Go back to Github and navigate to dist -> animate.exe and press "View Raw" to download this file.
8. Once the file is downloaded, go to your computers downloads folder and right click on the file to cut it.
9. Go to your extracted folder and paste the file into the dist folder. Press yes when prompted to replace the file.
10. Now you can click on animate.exe and the program will run. When completed, the animation will be saved as a .gif in the dist folder.

If you want to view the graphing function for the animation you can run graph.py in a virtual environment or in command line.

### Customization

If any edits want to be made to the code navigate to the animate.py file to make changes and run in a virtual environment.

## Example

Animation generated by animate.exe in green for 200 frames:


Graph generated by graph.py in blue for 10,000 iterations:


## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request if you find a bug, have a feature request, or would like to improve the project in any way.

## License

This project is licensed under the MIT License.