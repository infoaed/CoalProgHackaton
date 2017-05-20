<?php


//https://aavik.riigikogu.ee/api/ems/v1/volumes/drafts/search?count=1&limit=500

$dsn = 'pgsql:dbname=valitsus;host=127.0.0.1';
$user = 'postgres';
$password = 'pass';
$pdo = new PDO($dsn, $user, $password);
/*
$pdo->query('CREATE TABLE eelnoud (id serial PRIMARY KEY, mark varchar, title varchar, stage varchar, initiated bigint, modified bigint, f_id varchar, membership integer);');
$pdo->query('CREATE INDEX eelnoud_mark ON eelnoud(mark);');
die();*/

function scrape($url) {
	echo 'Scraping '.$url.PHP_EOL;
	return json_decode(file_get_contents($url));
}

$current = 0;
$prepared = $pdo->prepare('INSERT INTO eelnoud(mark, title, stage, initiated, modified, f_id, membership) VALUES(:mark, :title, :stage, :initiated, :modified, :fid, :membership)', array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
while(true) {
	$json = scrape('https://aavik.riigikogu.ee/api/ems/v1/volumes/drafts/search?count=1&limit=500&skip=' . $current);
	if(!$json->result) {
		break;
	}
	
	foreach($json->result as $res) {
		$bool = $prepared->execute(array(
			':mark' => $res->mark,
			':title' => $res->title,
			':stage' => $res->activeDraftStage,
			':initiated' => $res->initiated,
			':modified' => $res->lastModified,
			':fid' => $res->uuid,
			':membership' => $res->membership,
		));
		if(!$bool) {
			print_r($prepared->errorInfo());die();
		}
	}
	
	
	
	$current += 500;
}
