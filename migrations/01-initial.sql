create table category (
	id integer primary key autoincrement,
	name text
);

create table entry (
	id integer primary key autoincrement,
	category_id integer,
	name text,
	amount float,
	created_at timestamp current_timestamp
);