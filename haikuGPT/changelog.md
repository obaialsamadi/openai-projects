# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- ## [Unreleased] -->

## [1.1.0] - 2023-04-07

### Added

- dalle2 image generation: the program now generates an image based on the title of the Haiku
- added changelog file


### Fixed

- extract_title() function inconsistency: old function used to throw index out of range error depending on how many words a user inputs. fixed this by writing new function to extract title

### Changed

- changed user input code to now accept coma separated input to allow word combinations
- print(image_response): instead of printing the url for the generated image, it now automatically opens the URL after generating it


### Removed

- old extract_title() function
- old user input join method
- print(image_response)

<!-- 
[unreleased]: 
[1.1.0]: 
[1.0.0]:  -->

