CREATE DATABASE IF NOT EXISTS pbz2;
USE pbz2;

DROP TABLE IF EXISTS table_hospital_discharge;
DROP TABLE IF EXISTS table_human_data;
DROP TABLE IF EXISTS table_room_data;
DROP TABLE IF EXISTS table_room_transfer;
create table pbz2.table_hospital_discharge
(
    fullname          varchar(255) null,
    date_of_discharge date         not null,
    discharge_id      int          not null
        primary key,
    discharge_reason  varchar(255) not null,
    discharge_room    int          not null,
    constraint table_hospital_discharge_pk
        unique (fullname),
    constraint table_hospital_discharge_pk_2
        unique (discharge_room),
    constraint table_hospital_discharge_table_human_data_full_name_fk
        foreign key (fullname) references pbz2.table_human_data (full_name),
    constraint table_hospital_discharge_table_human_data_room_number_fk
        foreign key (discharge_room) references pbz2.table_human_data (room_number)
);




create table pbz2.table_human_data
(
    human_id                  int          not null
        primary key,
    gender                    varchar(20)  not null,
    age                       int          null,
    preliminary_diagnosis     varchar(255) not null,
    admission_to_the_hospital varchar(255) not null,
    arrival_date              date         null,
    approximate_growth        int          not null,
    hair_type                 varchar(100) not null,
    room_number               int          not null,
    full_name                 varchar(255) null,
    constraint table_human_data_pk
        unique (full_name),
    constraint table_human_data_pk_3
        unique (room_number)
);



create table pbz2.table_room_data
(
    room_number int          not null,
    room_id     int          not null
        primary key,
    room_type   varchar(100) not null,
    full_name   varchar(255) null,
    room_phone  int          not null,
    constraint table_room_data_pk
        unique (full_name),
    constraint table_room_data_pk_4
        unique (room_number),
    constraint table_room_data_table_human_data_full_name_fk
        foreign key (full_name) references pbz2.table_human_data (full_name),
    constraint table_room_data_table_human_data_room_number_fk
        foreign key (room_number) references pbz2.table_human_data (room_number)
);


create table pbz2.table_room_transfer
(
    transfer_date date         not null,
    `transfer id` int          not null
        primary key,
    transfer_from int          not null,
    transfer_to   int          not null,
    full_name     varchar(255) null,
    constraint table_room_transfer_pk
        unique (full_name),
    constraint table_room_transfer_table_human_data_full_name_fk
        foreign key (full_name) references pbz2.table_human_data (full_name)
);




