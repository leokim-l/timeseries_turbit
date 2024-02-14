from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


# It is sometimes necessary to generate aliases because of special characters
class Turbs(BaseModel):
    date: Optional[str] = Field(datetime, alias="Dat/Zeit")
    wind: Optional[str] = Field(str, alias="Wind_m/s")
    Rotor_rpm: str
    Leistung_kW: str
    azimut: Optional[str] = Field(str, alias="Azimut_°")
    turb_id: int
    prod1: Optional[str] = Field(int, alias="Prod. 1_kWh")
    prod2: Optional[str] = Field(int, alias="Prod. 2_kWh")
    BtrStd1: Optional[str] = Field(int, alias="BtrStd 1_h")
    BtrStd2: Optional[str] = Field(int, alias="BtrStd 2_h")
    Gen1: Optional[str] = Field(str, alias="Gen1-_°C")
    Lager: Optional[str] = Field(str, alias="Lager_°C")
    AusT: Optional[str] = Field(str, alias="Außen_°C")
    GetrT: Optional[str] = Field(str, alias="GetrT_°C")
    Status: bool
    Spann_V: str
    Spann_V1: Optional[str] = Field(str, alias="Spann_V.1")
    Spann_V2: Optional[str] = Field(str, alias="Spann_V.2")
    StromA: Optional[str] = Field(str, alias="Strom-_A")
    StromA1: Optional[str] = Field(str, alias="Strom-_A.1")
    StromA2: Optional[str] = Field(str, alias="Strom-_A.2")
    CosPh: str
    Abgabe_kWh: float
    Bezug_kWh: float
    KHzahl1: Optional[str] = Field(float, alias="KH-Zähl1_Imp")
    KHzahl1: Optional[str] = Field(float, alias="KH-Zähl2_Imp")
    KHdigiE_bit: Optional[str] = Field(float, alias="KH-DigiE_Bit")
    KHdigiI_bit: Optional[str] = Field(float, alias="KH-DigiI_Bit")
    KHana1: Optional[str] = Field(float, alias="KH-Ana-1")
    KHana2: Optional[str] = Field(float, alias="KH-Ana-2")
    KHana3: Optional[str] = Field(float, alias="KH-Ana-3")
    KHana4: Optional[str] = Field(float, alias="KH-Ana-4")
