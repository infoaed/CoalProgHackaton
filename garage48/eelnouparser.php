<?php

//ALTER TABLE mytable ADD COLUMN mycolumn character varying(50) NOT NULL DEFAULT 'foo';

$dsn = 'pgsql:dbname=valitsus;host=127.0.0.1';
$user = 'postgres';
$password = 'pass';
$pdo = new PDO($dsn, $user, $password);

/*$pdo->query('ALTER TABLE paevakord ADD COLUMN eelnou_mark varchar NULL;');
$pdo->query('CREATE TABLE paevakord_eelnoud (eelnoud_id integer, paevakord_id integer);');
$pdo->query('CREATE INDEX paevakord_eelnoud_eelnoud ON paevakord_eelnoud(eelnoud_id);');
$pdo->query('CREATE INDEX paevakord_eelnoud_paevakord ON paevakord_eelnoud(paevakord_id);');
die();
*/


$paevakordsSelect = $pdo->prepare("SELECT paevakord.idpaevakord, paevakord.pealkiri, istung.riigikogu_cf FROM paevakord JOIN istung ON istung.idistung=paevakord.idistung WHERE paevakord.pealkiri LIKE '%SE)%'", array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));

$bool = $paevakordsSelect->execute(array());
if(!$bool) {
	print_r($paevakordsSelect->errorInfo());die();
}
$paevakords = $paevakordsSelect->fetchAll();
$preparedSelect = $pdo->prepare('SELECT id FROM eelnoud WHERE mark=:mark AND membership=:membership', array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
$preparedUpdate = $pdo->prepare('UPDATE paevakord SET eelnou_mark=:mark WHERE idpaevakord=:id', array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
$preparedInsert = $pdo->prepare('INSERT INTO paevakord_eelnoud(eelnoud_id, paevakord_id) VALUES(:eelnou, :paevakord)', array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));

foreach($paevakords as $pi => $data) {
	echo 'Processing '.$pi.'/'.count($paevakords).PHP_EOL;
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
	
	foreach($marks as $mark) {
		$bool = $preparedUpdate->execute(array(
			':mark' => $mark,
			':id' => $data['idpaevakord']
		));
		if(!$bool) {
			print_r($preparedUpdate->errorInfo());die();
		}
		
		
		$bool = $preparedSelect->execute(array(
			':mark' => $mark,
			':membership' => $data['riigikogu_cf'],
		));
		if(!$bool) {
			print_r($preparedSelect->errorInfo());die();
		}
		$selectData = $preparedSelect->fetchAll();
		if(count($selectData) !== 1) {
			file_put_contents('log.txt', 'ERROR: '.$mark.'|'.$data['riigikogu_cf'].PHP_EOL, FILE_APPEND);
			echo 'ERROR'.PHP_EOL;
			continue;
		}
		$eelnouId = array_pop($selectData)['id'];
	
	
		$bool = $preparedInsert->execute(array(
			':eelnou' => $eelnouId,
			':paevakord' => $data['idpaevakord'],
		));
		if(!$bool) {
			print_r($preparedInsert->errorInfo());die();
		}
	}
	
	
	
	
/*
	if(count($marks) !== 1) {
		print_r($data);
		print_r($marks);
		print_r($parsed);
		echo PHP_EOL.PHP_EOL;
	}*/
	
	/*foreach($marks as $mark) {
	
	}

	
	file_put_contents('log.txt', $parsed.PHP_EOL, FILE_APPEND);
	echo $parsed.PHP_EOL;*/

}

