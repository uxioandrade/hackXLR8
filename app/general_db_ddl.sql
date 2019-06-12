CREATE TABLE user(
	varchar(20) id NOT NULL,

)

CREATE TABLE video(
	CHAR(20) id NOT NULL,
	DECIMAL(4,2) duration NOT NULL,
	PRIMARY KEY id
)

CREATE TABLE transcript(
	CHAR(20) id NOT NULL,
	CHAR(20) video NOT NULL,
	FOREIGN KEY video REFERENCES video(id)
	ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY id, video
)

CREATE TABLE summary(
	CHAR(10) id NOT NULL,
	CHAR(20) video NOT NULL,
	FOREIGN KEY video REFERENCES video(id)
	ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY id,video
)
