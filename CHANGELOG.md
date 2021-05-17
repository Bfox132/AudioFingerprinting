# Change Log

## [0.3.1] 2021 - 05 - 12

### Added
- align_files: like align, but takes two or more filenames/paths to align
- align_files tests
- addopts to pytest.ini file

### Changed
- tests: all write to tmpdir except for saving fingerprints

### Fixed
- Pydub linux file reading bug: throws IndexError where it should be CouldntDecodeError

## [0.3.0] 2021 - 05 - 02

### Added
- Locality_filter_prop: filters locality tuples by proportion of highest confidence to tuple confidence within each offset
- Locality tuples include individual confidences at the end of each tuple

## [0.2.2] 2021 - 05 - 02

### Fixed
- Locality, improperly sorted through tuple noise

## [0.2.1] 2021 - 04 - 28

### Fixed
- Locality, wasn't creating correct tuples

## [0.2.0] 2021 - 04 - 14

### Added
- metadata function
- Correlation based alignment and correcognize
- frequency threshold getter and static setter

### Changed
- "use_fingerprints" to "technique" that takes a string
- changed filter fingerprints in align to none to tell if user input is supplied
- Bumped urllib and Pillow

## [0.1.6] 2021 - 02 - 26

### Fixed
- Messed up version nums

## [0.1.5] 2021 - 02 - 26

### Added 
- fingerprinting and alignment windows

### Changed
- Sped up fingerprinting in tests
- Documentation all same style

### Fixed
- write shifted files loophole
- read write destination

## [0.1.4] 2021 - 02 - 05

### Added
- Github Actions
- Locality Fingerprinting

### Fixed
- recognize bug
- tests

## [0.1.3] 2021 - 01 - 27

### Added
- Args and kwargs for noise reduce

### Changed
- Visual Alignment weighting

### Fixed 
- Try except for write in aligns

## [0.1.2] 2020 - 12 - 29

### Fixed
- Writing total track
- target align bug

## [0.1.1] 2020 - 12 - 22

### Added
- Visual Calc_mse
- Visual Image Resizing
- Visual Volume Floor

## [0.1.0] 2020 - 12 - 18

### Added
- Tons of Stuff
- Many Tests
- There are previous versions, but I don't think anybody would care about them