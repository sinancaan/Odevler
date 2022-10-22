create table yapimci
(
id serial primary key,
yapimci_adi varchar(50) not null,
yapimci_mail varchar(100)
);

CREATE TABLE sarkilar
(
id serial PRIMARY KEY,
sarkici_adi varchar(50) not null,
sarki_adi VARCHAR(50) NOT NULL,
sarki_suresi INT NOT NULL,
sarki_turu VARCHAR(50),
album_adi varchar(50),
yapimci_id int,

    CONSTRAINT FK_YAPIMCI
        FOREIGN KEY (yapimci_id)
            REFERENCES yapimci (id)
);

insert into yapimci(yapimci_adi, yapimci_mail)
values('KALAN MUZIK', 'kalan@gmail.com');

insert into yapimci(yapimci_adi, yapimci_mail)
values('APPLE MUZIK', 'muzik@apple.com');

insert into yapimci(yapimci_adi, yapimci_mail)
values('NARLI PLAK', 'narlıp@gmail.com');

insert into sarkilar(sarkici_adi, sarki_adi, sarki_suresi, sarki_turu, album_adi, yapimci_id)
values('6IX9INE', 'GOOBA', 2.57, 'RAP', 'DUMMY', 2);

insert into sarkilar(sarkici_adi, sarki_adi, sarki_suresi, sarki_turu, album_adi, yapimci_id)
values('HAYKO CEPKIN', 'KABUL OLUR', 6, 'METAL', 'TANISMA BITTI', 1);

insert into sarkilar(sarkici_adi, sarki_adi, sarki_suresi, sarki_turu, album_adi, yapimci_id)
values('EMINEM', 'STAN', 4, 'RAP', 'EMINEMCIM', 3);

insert into sarkilar(sarkici_adi, sarki_adi, sarki_suresi, sarki_turu, album_adi, yapimci_id)
values('JUSTIN BIEBER', 'BABY', 4, 'POP', 'BABY', 2);

insert into sarkilar(sarkici_adi, sarki_adi, sarki_suresi, sarki_turu, album_adi, yapimci_id)
values('AEROSMITH', 'DREAM ON', 4, 'ROCK', 'TUBE', 3);

insert into sarkilar(sarkici_adi, sarki_adi, sarki_suresi, sarki_turu, album_adi, yapimci_id)
values('RIHANNA', 'DIAMOND', 4, 'POP', 'CUP', 2);

insert into sarkilar(sarkici_adi, sarki_adi, sarki_suresi, sarki_turu, album_adi, yapimci_id)
values('ORKUNDK', 'FRESH DUYGULARIN ADAMI', 4, 'RAP', 'TANRILAR BUNU ISTEDI', 1);

insert into sarkilar(sarkici_adi, sarki_adi, sarki_suresi, sarki_turu, album_adi, yapimci_id)
values('AEROSMITH', 'NOT AFFRAID', 4, 'ROCK', 'TUBE', 3);

select * from yapimci y;

select * from yapimci y where yapimci_adi = 'KALAN MUZIK';
select * from yapimci y where yapimci_adi = 'APPLE MUZIK';

select * from sarkilar s where sarkici_adi like '%KO%' or sarkici_adi like '%ko%';

select * from sarkilar s where id = 1 or id = 3;
select sarkici_adi  from sarkilar s where id = 1 or id = 3;

select * from yapimci y order by id;
select * from yapimci y order by id desc ;

select * from sarkilar s where id in(
	select id from sarkilar s2 where sarkici_adi like '%H%'
);

update sarkilar set sarki_suresi = 5 where id=3;

select concat(sarkici_adi, '/',sarki_adi,' by ', yapimci_adi) as SA_SA_YA, sarki_suresi from yapimci y 
left join sarkilar s on y.id = s.yapimci_id

select concat(sarkici_adi, '/', sarki_adi, ' - ', album_adi,' -- ', sarki_suresi) as SARKI_BILGILERI,
			(yapimci_adi,' : ', yapimci_mail) as YAPIMCI_BILGILERI from sarkilar s 
left join yapimci y on y.id = s.yapimci_id

SELECT concat(s.sarkici_adi, '/', s.sarki_adi) AS SARKI_INFO, y.yapimci_adi
FROM yapimci y
         LEFT JOIN sarkilar s on s.yapimci_id  = y.id where y.yapimci_adi  = 'APPLE MUZIK';
        
select s.sarki_suresi  from sarkilar s where s.album_adi = 'TUBE';
