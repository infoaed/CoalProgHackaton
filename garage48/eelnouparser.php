<?php

//ALTER TABLE mytable ADD COLUMN mycolumn character varying(50) NOT NULL DEFAULT 'foo';

$dsn = 'pgsql:dbname=valitsus;host=127.0.0.1';
$user = 'postgres';
$password = 'pass';
$pdo = new PDO($dsn, $user, $password);

/*
$pdo->query('ALTER TABLE paevakord ADD COLUMN eelnou_mark varchar NULL;');
die();
*/
/*
$pdo->query('CREATE TABLE eelnoud (id serial PRIMARY KEY, mark varchar, title varchar, stage varchar, initiated bigint, modified bigint, f_id varchar, membership integer);');
$pdo->query('CREATE INDEX eelnoud_mark ON eelnoud(mark);');
die();
*/

$pdo->query("SET NAMES iso-8859-1;");


$paevakords = $pdo->query("SELECT paevakord.idpaevakord, paevakord.pealkiri, istung.riigikogu_cf FROM paevakord JOIN istung ON istung.idistung=paevakord.idistung WHERE paevakord.pealkiri LIKE '%SE)%'");
foreach($paevakords as $data) {
	$parsed = substr($data['pealkiri'], 0, strrpos($data['pealkiri'], 'SE)'));
	$parsed = explode('(', $parsed);
	$parsed = trim(array_pop($parsed));
	$parsed = mb_convert_encoding($parsed, 'UTF-8', 'UTF-8');
	
	$marks = array($parsed);
	if(strpos($parsed, '&') !== false) {
		$marks = explode('&', $parsed);
	} elseif(strpos($parsed, 'ja') !== false) {
		$marks = explode('ja', $parsed);
	} elseif(strpos($parsed, ',') !== false) {
		$marks = explode(',', $parsed);
	}
	
	foreach($marks as $i => $mark) {
		$marks[$i] = (int) trim(str_replace('SE', '', $mark));
	} 

	if(count($marks) !== 1) {
		print_r($data);
		print_r($marks);
		print_r($parsed);
		echo PHP_EOL.PHP_EOL;
	}
	
	/*foreach($marks as $mark) {
	
	}

	
	file_put_contents('log.txt', $parsed.PHP_EOL, FILE_APPEND);
	echo $parsed.PHP_EOL;*/

}

