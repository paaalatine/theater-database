create or replace package util as
	FUNCTION create_requisite(
		requisiteName VARCHAR2,
		requisitePrice NUMBER)
		return NUMBER;
	PROCEDURE delete_requisite_by_id(req_id NUMBER);
	PROCEDURE delete_requisite_by_name(req_name VARCHAR2);

	FUNCTION create_post(postName VARCHAR2, salary NUMBER, serviceId NUMBER) RETURN NUMBER;
	FUNCTION create_performance(
		performanseName VARCHAR2,
		performancePrice NUMBER,
		description VARCHAR2)
		RETURN NUMBER;

	FUNCTION read_theater_expenses RETURN NUMBER;
	PROCEDURE print_theater_expenses;

	PROCEDURE delete_performance_by_id(per_id NUMBER);
	PROCEDURE delete_all_the_theater;

	FUNCTION create_timetable(eventType VARCHAR2, eventDate VARCHAR2, performanceId NUMBER) RETURN NUMBER;

	PROCEDURE read_timetable;

	PROCEDURE upd_prices_for_5_percent;
	PROCEDURE upd_prices_for_5_percent_down;

end util;

create or replace package body util as

	FUNCTION create_requisite(requisiteName VARCHAR2, requisitePrice NUMBER)
		RETURN NUMBER IS
		new_requisite_id NUMBER;
		BEGIN
			INSERT INTO REQUISITE(requisiteName, requisitePrice)
			VALUES(requisiteName, requisitePrice) RETURNING REQUISITE.REQUISITEID
			INTO new_requisite_id;
		RETURN(new_requisite_id);
	END create_requisite;

	PROCEDURE delete_requisite_by_id(req_id NUMBER) AS
		BEGIN
			DELETE FROM REQUISITE WHERE requisiteId = req_id;
		END;


	PROCEDURE delete_requisite_by_name(req_name VARCHAR2) AS
		BEGIN
			DELETE FROM REQUISITE WHERE REQUISITENAME = req_name;
		END;


	FUNCTION create_performance(
		performanseName VARCHAR2,
		performancePrice NUMBER,
		description VARCHAR2)
		RETURN NUMBER IS new_performance_id NUMBER;
		BEGIN
			INSERT INTO PERFORMANCE(performanseName, performancePrice, description)
			VALUES(performanseName, performancePrice, TO_BLOB(description)) RETURNING PERFORMANCE.PERFORMANCEID
			INTO new_performance_id;
			RETURN(new_performance_id);
		END create_performance;


	PROCEDURE delete_performance_by_id(per_id NUMBER) AS
		BEGIN
			DELETE FROM PERFORMANCE WHERE performanceId = per_id;
		END;


	FUNCTION create_post(postName VARCHAR2, salary NUMBER, serviceId NUMBER)
		RETURN NUMBER IS
		new_post_id NUMBER;
	BEGIN
		INSERT INTO POST(postName, salary, serviceId)
		VALUES (postName, salary, serviceId) RETURNING POST.POSTID INTO new_post_id;
		RETURN (new_post_id);
	END create_post;


	FUNCTION read_theater_expenses RETURN NUMBER IS
		req_summary NUMBER;
		post_summary NUMBER;
		BEGIN
			SELECT SUM(REQUISITEPRICE) INTO req_summary FROM REQUISITE;
			SELECT SUM(SALARY) INTO post_summary FROM POST;
			RETURN(req_summary + post_summary);
		END;

	PROCEDURE print_theater_expenses as
		BEGIN
			DBMS_OUTPUT.PUT_LINE('Theater Expenses:');
			DBMS_OUTPUT.PUT_LINE( UTIL.read_theater_expenses );
		END;

	PROCEDURE delete_all_the_theater AS
		BEGIN
			DELETE FROM BOOKING;
			DELETE FROM CAST;
			DELETE FROM DECORATION;
			DELETE FROM PERFORMANCE;
			DELETE FROM PLACE;
			DELETE FROM POST;
			DELETE FROM REQUISITE;
			DELETE FROM SERVICE;
			DELETE FROM STAFF;
			DELETE FROM TIMETABLE;
		END;

	FUNCTION create_timetable(
		eventType VARCHAR2,
		eventDate VARCHAR2,
		performanceId NUMBER) RETURN NUMBER IS
		timetable_id NUMBER;
		BEGIN
			INSERT INTO TIMETABLE(eventType, eventDate, performanceId)
				VALUES (eventType, TO_DATE(eventDate, 'DD/MM/YYYY'), performanceId) RETURNING TIMETABLE.EVENTID
			INTO timetable_id;
			RETURN (timetable_id);
		END;

	PROCEDURE read_timetable AS
		begin
			DBMS_OUTPUT.PUT_LINE('Timetable:');
			DBMS_OUTPUT.PUT_LINE('EventID | EventType | EventDate | PerformanceId');
			for time in (select * from TIMETABLE) loop
			DBMS_OUTPUT.PUT_LINE(time.EVENTID || ' | ' || time.EVENTTYPE || ' | ' || time.EVENTDATE || ' | ' || time.PERFORMANCEID);
			end loop;
		end;

	PROCEDURE upd_prices_for_5_percent AS
		BEGIN
			UPDATE REQUISITE
				SET REQUISITEPRICE = REQUISITEPRICE * 1.05;
			UPDATE POST
				SET SALARY = SALARY * 1.05;
			UPDATE PERFORMANCE
				SET PERFORMANCEPRICE = PERFORMANCEPRICE * 1.05;
		END;

	PROCEDURE upd_prices_for_5_percent_down AS
		BEGIN
			UPDATE REQUISITE
				SET REQUISITEPRICE = REQUISITEPRICE * 0.95;
			UPDATE POST
				SET SALARY = SALARY * 0.95;
			UPDATE PERFORMANCE
				SET PERFORMANCEPRICE = PERFORMANCEPRICE * 0.95;
		END;

END util;