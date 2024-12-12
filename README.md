# Color Separator

A simple Python application that separates the colors in an image and saves them as individual images. This tool uses the Pillow library for image processing and Tkinter for the graphical user interface.

## Features

- Select an image file (supports PNG, JPG, JPEG, BMP formats).
- Separate unique colors in the image.
- Save each color as a separate PNG file in a user-defined output directory.
- Simple and intuitive user interface.

## Requirements

- Python 3.x
- Pillow
- NumPy
- Tkinter (comes pre-installed with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/color-separator.git
   cd color-separator
   ```

2. Install the required packages:
   ```bash
   pip install Pillow numpy
   ```

## Usage

1. Run the application:
   ```bash
   python Color\ Separator.py
   ```

2. Click on "Set Output Directory" to choose where the separated images will be saved.

3. Click on "Select Image" to choose an image file.

4. The application will process the image and save the separated colors in the specified output directory.

5. You can open the output directory directly from the application by clicking "Open Directory".

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pillow](https://python-pillow.org/) - The Python Imaging Library (PIL) fork.
- [NumPy](https://numpy.org/) - The fundamental package for scientific computing with Python.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - The standard GUI toolkit for Python.
