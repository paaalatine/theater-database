CREATE OR REPLACE TYPE Description AS OBJECT
(
	TEXTED CLOB,
	PIC BLOB,
	sale_date DATE,
	MEMBER PROCEDURE set_all(s_TEXTED VARCHAR2, s_PIC BLOB, s_sale_date DATE),
	MEMBER FUNCTION get_poster_as_json RETURN VARCHAR2,
	MEMBER FUNCTION get_image RETURN BLOB,
	MEMBER FUNCTION get_date_of_presale RETURN DATE
);

CREATE OR REPLACE TYPE BODY Description AS
	MEMBER PROCEDURE set_all(s_TEXTED VARCHAR2, s_PIC BLOB, s_sale_date DATE) AS
		BEGIN
			TEXTED = json_object('TEXT' VALUE s_TEXTED);
			PIC = s_PIC;
			sale_date = s_sale_date;
		END;
	MEMBER FUNCTION get_poster_as_json RETURN VARCHAR2 IS
		json_data VARCHAR2;
		BEGIN
			json_data := json_object('TEXT' VALUE TEXTED,
									 'PIC'  VALUE PIC,
									 'SALEDATE' VALUE sale_date
			FORMAT JSON);
			RETURN(json_data);
		END;

	MEMBER FUNCTION get_image RETURN BLOB IS
		BEGIN
			RETURN(PIC);
		END;

	MEMBER FUNCTION get_date_of_presale RETURN DATE IS
		BEGIN
			RETURN(sale_date);
		END;
END ;