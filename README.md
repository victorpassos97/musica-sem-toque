# Música sem Toque
Projeto de um controlador de tocador de música utilizando gestos de cabeça.
Projeto criado para a discplina PCS3559/PCS3859 - Tecnologias para Aplicações
Interativas 2020.

## Documentação

* Raspberry Pi: <https://www.raspberrypi.org>
* Giroscópio e Acelerômetro: <https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf>
* Tutorial de leituras do sensor: <https://makersportal.com/blog/2019/11/11/raspberry-pi-python-accelerometer-gyroscope-magnetometer>

## Setup

É preciso habilitar a interface I2C do Raspberry nas configurações.

Ligação dos pinos

| MPU6050 | Raspbery Pi |
| ----- | ----- |
| VCC | pin 1 |
| GND | pin 6 |
| SCL | pin 5 |
| SDA | pin 3 |
| XDA | NC |
| XCL | NC |
| ADD | NC |
| INT | NC |
