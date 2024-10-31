# umi-grip-controller


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/erikhelmut/actuated-umi">
    <img src="docs/python_dynamixel_sdk_logo.png" alt="umi-grip-controller" height="170">
  </a>

  <h3 align="center">Python controller for the actuated UMI gripper.</h3>

  <p align="center">
    Elevate your robotics projects with umi-grip-contoller -- a powerful and user-friendly Python wrapper for the Dynamixel SDK libary, designed to effortlessly control the actuated UMI gripper.
    <br />
    <a href="https://github.com/erikhelmut/actuated-umi"><strong>Actuated UMI Gripper »</strong></a>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ol>
        <li>
          <a href="#prerequisites">Prerequisites</a>
        </li>
        <li>
          <a href="#hardware-setup">Hardware Setup</a>
        </li>
        <li>
          <a href="#installation">Installation</a>
        </li>
      </ol>
    </li>
    <li>
      <a href="#usage">Usage</a>
    </li>
    <li>
      <a href="#contribution">Contribution</a>
    </li>
  </ol>
</details>


<!-- INTRODUCTION -->
## Introduction
<a href="https://github.com/erikhelmut/umi-grip-controller">umi-grip-controller</a> is a Python wrapper for the <a href="https://github.com/ROBOTIS-GIT/DynamixelSDK">Dynamixel SDK library</a>, specifically crafted to control <a href="https://github.com/erikhelmut/actuated-umi">actuated UMI gripper</a> powered by the <a href="https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/">Dynamixel XL430-W250-T motor</a>. This library is a fork of <a href="https://github.com/TimSchneider42/python-rhp12rn-controller/tree/master">python-rhp12rn-controller</a>. It provides a high-level API that simplifies motor control through a `UMIGripConnector` class, which establishes and manages serial connections, and a `UMIGrip` class that offers direct access to frequently used control parameters. Users can read and write motor control fields easily, enabling quick setup for common robotic manipulation tasks. Although currently optimized for the Dynamixel XL430-W250-T motor, the library's modular design can be extended to accommodate additional Dynamixel motor types.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
Make sure you have a working Python 3 installation. If not, follow the instructions on the <a href="https://www.python.org/downloads/">Python 3 download page</a>.

### Hardware Setup
To use the umi-grip-controller library, you need to have an <a href="https://github.com/erikhelmut/actuated-umi">actuated UMI gripper</a> powered by the Dynamixel XL430-W250-T motor. The actuated UMI gripper is a low-cost, modular, and open-source robotic gripper designed to work with the <a href="https://umi-gripper.github.io">Universal Manipulation Interface (UMI)</a>. 

The actuated UMI gripper is controlled via a <a href="https://emanual.robotis.com/docs/en/parts/interface/u2d2_power_hub/">U2D2 Power Hub Board</a>, which connects to the gripper's Dynamixel motor via a 4-pin JST EH cable. The U2D2 Power Hub Board is connected to a computer via a USB cable, allowing the user to send commands to the gripper using the Dynamixel SDK library.


### Installation

#### Step 0: Create a workspace if you don't have one
```sh
mkdir -p ~/your_workspace/src
```

#### Step 1: Set up a virtual environment
```sh
cd ~/your_workspace
python3 -m venv venv
source venv/bin/activate
```

#### Step 2: Clone the Dynamixel SDK repository into your workspace
```sh
cd ~/your_workspace/src
git clone git@github.com:ROBOTIS-GIT/DynamixelSDK.git
```

#### Step 3: Build and install the Dynamixel SDK
```sh
cd ~/your_workspace/src/DynamixelSDK/python
python3 -m pip install --upgrade build
sudo python3 -m build
pip3 install dist/dynamixel_sdk-3.7.51.tar.gz
```

#### Step 4: Clone the umi-grip-controller repository into your workspace
```sh
cd ~/your_workspace/src
git clone git@github.com:erikhelmut/umi-grip-controller.git
```

#### Step 5: Build and install the umi-grip-controller library
```sh
cd ~/your_workspace/src/umi-grip-controller
sudo python3 -m build
pip3 install dist/umigrip-1.0.0.tar.gz
```

## Usage

First, create a `UMIGRIPConnector` instance and call the `connect()` function to establish a serial connection to the gripper:

```python
from umigrip import UMIGRIPConnector

connector = UMIGRIPConnector(device="/dev/ttyUSB0", baud_rate=57600, dynamixel_id=1)
connector.connect()
...
connector.disconnect()
```

`UMIGRIPConnector` instances can also be used as context managers:

```python
with UMIGRIPConnector(device="/dev/ttyUSB0", baud_rate=57600, dynamixel_id=1) as connector:
    ...
```

The `connector` object allows reading and writing of arbitrary addresses of the gripper's control table:

```python
print(connector.read_field("torque_enable"))
connector.write_field("torque_enable", 1)
print(connector.read_field("torque_enable"))
```

For a comprehensive list of its entries, refer to <https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/>.
Alternatively, all entries are listed in `xl430w250t_connector.py`.
Note that the motors have to be disabled (`"torque_enabled"` has to be set to 0) for EEPROM values to be written, while RAM values can be written at any time.

For convenience, the `UMIGRIP` class provides direct access to the most commonly used fields:

```python
import time
from umigrip import UMIGRIP

gripper = UMIGRIP(connector)
gripper.torque_enabled = True
gripper.goal_position = 1.0
time.sleep(3.0)
gripper.torque_enabled = False
```

For a full example of the usage of this package, refer to `example/open_close.py`.


<!-- CONTRIBUTION -->
## Contribution
We welcome contributions to this repository. If you would like to contribute, please <a href="https://github.com/erikhelmut/umi-grip-controller/fork">fork</a> this repository and submit a <a href="https://github.com/erikhelmut/umi-grip-controller/compare">pull request</a> with your changes.