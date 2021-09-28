# f1-telemetry-simulator
Program designed to read in Codemasters F1 telemetry data, and output improvements to car setups.

## Problem Statement

Codemasters provides 5 preset builds, as well as the option of a custom preset. Codemasters also provides a UDP telemetry data option which can output a variety of live data that can be used to help track your performance in real time. It would be helpful to use this telemetry data to determine an ideal build for your car, given your personal performance over a period of time.

## Relevant Links

[Motorsport Giant Formula 1 using AWS - A Case Study](https://www.linkedin.com/pulse/motorsport-giant-formula-1-using-aws-case-study-archishman-ghosh) - Get telemetry data delivered to Kinesis for future processing.
[f1-2019-telemetry package](https://f1-2019-telemetry.readthedocs.io/en/latest/) - A well documented Python implementation of 2019 telemetry written by Sidney Cadot.

## AWS Services to consider

* Kinesis Data Streams - useful for receiption of UDP telemetry
* Lambda - useful for processing UDP telemetry
