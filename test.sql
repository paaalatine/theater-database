INSERT INTO SERVICE (SERVICENAME) VALUES ('buffet');
INSERT INTO SERVICE (SERVICENAME) VALUES ('wardrobe');
INSERT INTO SERVICE (SERVICENAME) VALUES ('toilet');
--
declare
   result number;
BEGIN
    result := UTIL.CREATE_REQUISITE('zombie head', 120);
    result := UTIL.CREATE_REQUISITE('pink hat', 400);
    result := UTIL.CREATE_REQUISITE('chair', 600);
    result := UTIL.CREATE_REQUISITE('chair', 600);
    result := UTIL.CREATE_REQUISITE('dead mouse', 300);

    result := UTIL.CREATE_PERFORMANCE('Athello', 3000, '990');
    result := UTIL.CREATE_PERFORMANCE('Snegurochka', 3500, 'bea');
    result := UTIL.CREATE_PERFORMANCE('Romario and Dakotta', 4000, '34eb');
    result := UTIL.CREATE_PERFORMANCE('Lady Makbett', 3000, '1234');

    result := util.create_post('buffetter', 30000, 1);
    result := util.create_post('wardrobber', 25000, 2);
    result := util.create_post('toiletterino', 30000, 3);
    UTIL.UPDATE_PRICES_FOR_5_PERCENT;
END;
--
declare
   result number;
BEGIN
    result := UTIL.create_timetable('dress rehearsal', '05.10.2017', 1);
    result := UTIL.create_timetable('repetition', '06.10.2017', 2);
    result := UTIL.create_timetable('repetition', '09.10.2017', 1);
    result := UTIL.create_timetable('performance', '10.10.2017', 1);
END;