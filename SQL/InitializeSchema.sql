create table Captured_Images
(
    Captured_Time_UTC DATETIME not null,
    Latitude          REAL     not null,
    Longitude         REAL     not null,
    Valid_Image       BOOL default TRUE,
    primary key (Captured_Time_UTC, Latitude, Longitude)
);


