var tsl2561 = require('tsl2561');
 
var device = "/dev/i2c-1"
var address = 0x39;
 
var sensor = new tsl2561.Tsl2561(device, address);
 
var luminosity = sensor.lux();