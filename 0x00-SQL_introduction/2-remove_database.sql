# Check if the database exists
IF EXISTS (SELECT * FROM information_schema.schemata WHERE schema_name = 'hbtn_0c_0') THEN
	  # Drop the database if it exists
	  DROP DATABASE hbtn_0c_0;
END IF;
