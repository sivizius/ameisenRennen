from socket import *

KACI0103                                =   []
KACI0103                                +=  [[   0, TYPE_ASCII,     8,  "Module Name",                    0,      0,  None, False,  "Module Name,No range" ]]
KACI0103                                +=  [[   8, TYPE_ASCII,     4,  "User Name",                      0,      0,  None, False,  "User Name,the abbreviation of user,ASCII" ]]
KACI0103                                +=  [[  12, TYPE_HEX,       4,  "Serial Number",                  0,      0,  None, False,  "Serial Number,No range" ]]
KACI0103                                +=  [[  16, TYPE_HEX,       4,  "Software Version",               0,      0,  None, False,  "Software Version,No range" ]]
KACI0103                                +=  [[  20, TYPE_BITS,      0,  "Startup H-Pedel",                0,      1,  None, True,   "0:disable,1:enable,Startup H-Pedel Function,if throttle has effective signal when power-on,disable output and report this fault." ]]
KACI0103                                +=  [[  20, TYPE_BITS,      1,  "Brake H-Pedel",                  0,      1,  None, True,   "0:disable,1:enable,Brake H-Pedel,if throttle has effective signal when release brake,disable output and report this fault." ]]
KACI0103                                +=  [[  20, TYPE_BITS,      2,  "NTL H-Pedel",                    0,      1,  None, True,   "0:disable,1:enable,Neutral H-Pedel,if throttle has effective signal from N to Drive,disable output and report this fault." ]]
KACI0103                                +=  [[  20, TYPE_BITS,      5,  "Two Speed",                      0,      1,  None, True,   "0:disable,1:enable,if enable,two Speed Gear:HighSpeed and Low Speed." ]]
KACI0103                                +=  [[  21, TYPE_BITS,      0,  "Foot Switch",                    0,      1,  None, True,   "0:disable,1:enable,if switch on,the throttle pedal is effective." ]]
KACI0103                                +=  [[  21, TYPE_BITS,      1,  "SW Level",                       0,      1,  None, False,  "0:SW Low-Level effective;1:SW High-Level effective" ]]
KACI0103                                +=  [[  21, TYPE_BITS,      3,  "0,HIM;1,KIM",                    0,      1,  None, False,  "Controller Type,0:HIM;1:KIM." ]]
KACI0103                                +=  [[  21, TYPE_BITS,      4,  "Exchange Encoder Phase",         0,      1,  None, True,   "0:disable,1:enable,Exchange Encoder Phase sequence" ]]
KACI0103                                +=  [[  21, TYPE_BITS,      5,  "Exchange Motor Phase",           0,      1,  None, True,   "0:disable,1:enable,Exchange Motor Phase sequence" ]]
KACI0103                                +=  [[  21, TYPE_BITS,      6,  "Anti Slip Func",                 0,      1,  None, True,   "0:disable,1:enable," ]]
KACI0103                                +=  [[  22, TYPE_UNSIGNED,  1,  "Startup Wait Time",              0,     20,  None, True,   "Startup Wait Time,Range 0~20." ]]
KACI0103                                +=  [[  23, TYPE_UNSIGNED,  2,  "Controller Volt",                0,    612,  None, False,  "Controller Voltage,Range 0~612" ]]
KACI0103                                +=  [[  25, TYPE_UNSIGNED,  2,  "Low Volt",                       0,   1000,  None, True,   "The min Voltage value of reporting this fault" ]]
KACI0103                                +=  [[  27, TYPE_UNSIGNED,  2,  "Over Volt",                      0,   1000,  None, True,   "The max Voltage value of reporting this fault" ]]
KACI0103                                +=  [[  33, TYPE_UNSIGNED,  2,  "Hall_A_Zero",                  474,   2200,  None, False,  "Phase A Zero current，范围474(10位)~2200(12位)" ]]
KACI0103                                +=  [[  35, TYPE_UNSIGNED,  2,  "Hall_B_Zero",                  474,   2200,  None, False,  "Phase B Zero current，范围474(10位)~2200(12位)" ]]
KACI0103                                +=  [[  40, TYPE_UNSIGNED,  2,  "RZ_A_Zero",                    474,   2200,  None, False,  "PHASE_A_RZ_CURRENT Zero内阻取样A相电流零点，范围474(10位)~2200(12位)" ]]
KACI0103                                +=  [[  42, TYPE_UNSIGNED,  2,  "RZ_B_Zero",                    474,   2200,  None, False,  "PHASE_B_RZ_CURRENT Zero内阻取样B相电流零点，范围474(10位)~2200(12位)" ]]
KACI0103                                +=  [[  44, TYPE_UNSIGNED,  2,  "RZ_C_Zero",                    474,   2200,  None, False,  "PHASE_C_RZ_CURRENT Zero内阻取样C相电流零点，范围474(10位)~2200(12位)" ]]
KACI0103                                +=  [[  37, TYPE_UNSIGNED,  1,  "Current Percent",               20,    100,  None, True,   "Current Percent,Range 20~100%" ]]
KACI0103                                +=  [[  38, TYPE_UNSIGNED,  1,  "Battry Current Limit",          20,    100,  None, True,   "Battry Current Limit,Limit the max value of Battry Current,Range 20~100" ]]
KACI0103                                +=  [[  39, TYPE_UNSIGNED,  1,  "Battry Current Weak",           20,    100,  None, True,   "Battry Current Limit Weaking,the rest per of Weaking Current,generally 1.15 times of Low Volt CUT,Range 20~100." ]]
KACI0103                                +=  [[  40, TYPE_UNSIGNED,  2,  "Internal Phase_A Zero",        474,   2200,  None, False,  "Internal Phase_A Zero.Range 474~2200." ]]
KACI0103                                +=  [[  42, TYPE_UNSIGNED,  2,  "Internal Phase_B Zero",        474,   2200,  None, False,  "Internal Phase_B Zero.Range 474~2200." ]]
KACI0103                                +=  [[  44, TYPE_UNSIGNED,  2,  "Internal Phase_C Zero",        474,   2200,  None, False,  "Internal Phase_C Zero.Range 474~2200." ]]
KACI0103                                +=  [[  92, TYPE_UNSIGNED,  1,  "TPS Low",                        0,     20,  None, True,   "If lower than the value,report the fault of TPS Type,Range 0~20%" ]]
KACI0103                                +=  [[  93, TYPE_UNSIGNED,  1,  "TPS High",                      80,    100,  None, True,   "If hifher than the value,report the fault of TPS Type,Range 80~100%" ]]
KACI0103                                +=  [[  94, TYPE_UNSIGNED,  1,  "Acc Speed",                     10,    100,  None, True,   "Acc Speed，the smaller the value is,the faster the speed accelerate,Range 10~100." ]]
KACI0103                                +=  [[  95, TYPE_UNSIGNED,  1,  "TPS Type",                       0,      3,  None, True,   "TPS Type,0:None,1:0-5V,2:1-4V,3:0-5K" ]]
KACI0103                                +=  [[  96, TYPE_UNSIGNED,  1,  "TPS Dead Low",                   0,     80,  None, True,   "TPS Dead Zone Low,Range 0~40%." ]]
KACI0103                                +=  [[  97, TYPE_UNSIGNED,  1,  "TPS Dead High",                120,    200,  None, True,   "TPS Dead Zone High,Range 60~100%." ]]
KACI0103                                +=  [[  98, TYPE_UNSIGNED,  1,  "TPS Forw MAP",                   0,    100,  None, True,   "TPS Forward MAP,Range 0~100,max TPS per when TPS is 50% Forward,determine Curvity." ]]
KACI0103                                +=  [[  99, TYPE_UNSIGNED,  1,  "TPS Rev MAP",                    0,    100,  None, True,   "TPS Reversed MAP,Range 0~100,max TPS per when TPS is 50% Reversed,determine Curvity." ]]
KACI0103                                +=  [[ 105, TYPE_UNSIGNED,  2,  "Max Output Fre",                 0,    300,  None, True,   "Max Output Frequency,Range 0~300Hz" ]]
KACI0103                                +=  [[ 107, TYPE_UNSIGNED,  2,  "Max Speed",                      0,  60000,  None, True,   "Max speed,Range 0~60000rpm" ]]
KACI0103                                +=  [[ 109, TYPE_UNSIGNED,  1,  "H-Speed Forw Speed%",           30,    100,  None, True,   "High Speed Forward Speed Limit,Range 30~100" ]]
KACI0103                                +=  [[ 110, TYPE_UNSIGNED,  1,  "H-Speed Rev  Speed%",           20,    100,  None, True,   "High Speed Reverse Speed Limit,Range 20~100" ]]
KACI0103                                +=  [[ 111, TYPE_UNSIGNED,  1,  "L-Speed Forw Speed%",           30,    100,  None, True,   "Low Speed Forward Speed Limit,Range 30~100" ]]
KACI0103                                +=  [[ 112, TYPE_UNSIGNED,  1,  "L-Speed Rev  Speed%",           20,    100,  None, True,   "Low Speed Reverse Speed Limit,Range 20~100" ]]
KACI0103                                +=  [[ 140, TYPE_UNSIGNED,  2,  "Voltage dUqKp",                  0,    500,  None, True,   "Voltage Circle Proportion Kp.Range 0~500." ]]
KACI0103                                +=  [[ 142, TYPE_UNSIGNED,  2,  "Voltage dUqKi",                  0,     50,  None, True,   "Voltage Circle Integral Ki.Range 0~50." ]]
KACI0103                                +=  [[ 144, TYPE_UNSIGNED,  2,  "Voltage dUqErrMax",             50,    500,  None, True,   "Voltage Circle dUqErrMax.Range 50~500." ]]
KACI0103                                +=  [[ 170, TYPE_UNSIGNED,  2,  "PH Mode Kp",                     0,   8192,  None, True,   "Position_Hold mode Kp.Range 0~8192." ]]
KACI0103                                +=  [[ 172, TYPE_UNSIGNED,  2,  "PH Mode Kd",                     0,   8192,  None, True,   "Position_Hold mode Kp.Range 0~8192." ]]
KACI0103                                +=  [[ 174, TYPE_UNSIGNED,  2,  "PH Mode Errmax",                 0,   8192,  None, True,   "Position_Hold mode Errmax.Range 0~8192." ]]
KACI0103                                +=  [[ 176, TYPE_UNSIGNED,  2,  "PH Mode SlipMax",                0,    150,  None, True,   "Position_Hold mode SlipMax.Range 0~8192." ]]
KACI0103                                +=  [[ 228, TYPE_UNSIGNED,  2,  "Brk_Speed Limit",               50,    500,  None, True,   "Brk Speed Limit,run regen brk when Motor speed is higher than this,Range 50~500" ]]
KACI0103                                +=  [[ 230, TYPE_UNSIGNED,  1,  "RLS_TPS Brk Per%",               0,     50,  None, True,   "RLS_TPS Braking Percent,the per of Rleasing Pedel BRK in max BRK,Range 0~50" ]]
KACI0103                                +=  [[ 231, TYPE_UNSIGNED,  1,  "NTL Brk Per%",                   0,     50,  None, True,   "NTL Braking Percent,the per of Neutral Braking in max BRK,Range 0~50" ]]
KACI0103                                +=  [[ 239, TYPE_UNSIGNED,  1,  "Accel Time",                     0,    250,  None, True,   "Accel Time,the time of TPS Torque from 0 to max,0.1~25.0s,accuracy 0.1s" ]]
KACI0103                                +=  [[ 240, TYPE_UNSIGNED,  1,  "Accel Release Time",             0,    250,  None, True,   "Accel Release Time,the time of TPS Torque form max to 0,0.1~25.0s,accuracy 0.1s" ]]
KACI0103                                +=  [[ 241, TYPE_UNSIGNED,  1,  "Brake Time",                     0,    250,  None, True,   "Brake Time,Accel Time,the time of Brake Torque from 0 to max,0.1~25.0s,accuracy 0.1s" ]]
KACI0103                                +=  [[ 242, TYPE_UNSIGNED,  1,  "Brake Release Time",             0,    250,  None, True,   "Brake Release Time,the time of Brake Torque form max to 0,0.1~25.0s,accuracy 0.1s" ]]
KACI0103                                +=  [[ 243, TYPE_UNSIGNED,  1,  "BRK_SW Brk Per%",                0,    100,  None, True,   "BRK_SW Braking Percent,the per of BRK_SW in max braking,Range 0~100" ]]
KACI0103                                +=  [[ 244, TYPE_UNSIGNED,  1,  "IVT Braking Percent%",           0,    100,  None, True,   "IVT Braking Percent,the per of IVT in max braking,Range 0~100" ]]
KACI0103                                +=  [[ 245, TYPE_UNSIGNED,  1,  "Compensation Percent%",          0,    100,  None, True,   "Compensation Percent,the per of Anti Slip Compensation in max braking,Range 0~100" ]]
KACI0103                                +=  [[ 246, TYPE_UNSIGNED,  2,  "IVT BRK Max Motor RPM",          0,   3000,  None, True,   "IVT BRK Max Motor RPM,Range 0~3000rpm" ]]
KACI0103                                +=  [[ 248, TYPE_UNSIGNED,  2,  "IVT BRK Min Motor RPM",          0,    500,  None, True,   "IVT BRK Min Motor RPM,Range 0~500rpm" ]]
KACI0103                                +=  [[ 250, TYPE_UNSIGNED,  2,  "Speed Circle Torque Kp",         0,  32767,  None, True,   "Speed Circle Kp in Torque Mode，the value higher,the motor more faster response.Range 0~32767" ]]
KACI0103                                +=  [[ 252, TYPE_UNSIGNED,  2,  "Speed Circle Torque Ki",         0,  32767,  None, True,   "Speed Circle Ki in Torque Mode，the value higher,the motor more faster response.Range 0~32767" ]]
KACI0103                                +=  [[ 254, TYPE_UNSIGNED,  2,  "Speed Circle Torque ErrMax",    50,   4095,  None, True,   "Speed Circle ErrMax Torque Mode，the value higher,the motor more faster response.Range 50~4095" ]]
KACI0103                                +=  [[ 268, TYPE_UNSIGNED,  1,  "Motor Poles",                    2,     32,  None, True,   "Motor Poles,The pole number*2,Range 2~32" ]]
KACI0103                                +=  [[ 269, TYPE_UNSIGNED,  1,  "Speed Sensor Type",              0,      4,  None, True,   "Speed Sensor Type,0:NO,1:Quadrature encoder,2:Hall,3:Resolver" ]]
KACI0103                                +=  [[ 270, TYPE_UNSIGNED,  2,  "Encoder Pulses",                 0,  65535,  None, True,   "Encoder Pulses,Range 0~65535" ]]
KACI0103                                +=  [[ 272, TYPE_UNSIGNED,  1,  "Resolver Poles",                 2,     32,  None, True,   "Resolver Poles,he pole number*2,Range 2~32" ]]
KACI0103                                +=  [[ 300, TYPE_UNSIGNED,  4,  "Motor Nominal Tr",            1000,  15000,  None, True,   "Motor Nominal Tr，Motor Nominal Rotor Time.Range 1000~15000." ]]
KACI0103                                +=  [[ 304, TYPE_UNSIGNED,  4,  "Motor Max Tr",                1000,  15000,  None, True,   "Motor Max Tr， Motor Max Rotor Time.,Range 1000~15000" ]]
KACI0103                                +=  [[ 308, TYPE_UNSIGNED,  2,  "Motor No-load Curr",             5,    150,  None, True,   "Motor No-load Current，Motor Nominal，unit A,Range 5~150" ]]
KACI0103                                +=  [[ 310, TYPE_UNSIGNED,  2,  "Min Excitation Curr",            5,    150,  None, True,   "Min Excitation Current.,Range 5~150" ]]
KACI0103                                +=  [[ 312, TYPE_UNSIGNED,  2,  "Start-up Slip Max RPM",         10,    300,  None, True,   "Motor Start-up,the limit Slip RPM.Range 10~300" ]]
KACI0103                                +=  [[ 314, TYPE_UNSIGNED,  2,  "Update Slip Max RPM",           10,    300,  None, True,   "the limit Slip RPM increased after Weak magnetic.,Range 10~300" ]]
KACI0103                                +=  [[ 316, TYPE_UNSIGNED,  2,  "Nominal Slip Max RPM",          10,    300,  None, True,   "Motor Nominal Slip Max RPM.Range 10~300" ]]
KACI0103                                +=  [[ 318, TYPE_UNSIGNED,  1,  "Motor Temp Sersor",              0,      1,  None, True,   "Motor Temp Sersor,0:None;1:KTY83-122;2:KTY84-130 or 150." ]]
KACI0103                                +=  [[ 319, TYPE_UNSIGNED,  1,  "High Temp Cut℃",                60,    170,  None, True,   "Motor High Temp Cut Temp,nominal value 130℃,Range 60~170" ]]
KACI0103                                +=  [[ 320, TYPE_UNSIGNED,  1,  "High Temp Resume",              60,    170,  None, True,   "Motor High Temp Resume Temp,nominal value 110℃,Range 60~170" ]]
KACI0103                                +=  [[ 321, TYPE_UNSIGNED,  1,  "High Temp Str℃",                 0,    170,  None, True,   "Motor High Temp Str Temp,nominal value 100℃,Range 0~170" ]]
KACI0103                                +=  [[ 322, TYPE_UNSIGNED,  1,  "High Temp Weak%",                0,    100,  None, True,   "Motor High Temp Weak Percent,nominal value 50%,Range 0~100" ]]
