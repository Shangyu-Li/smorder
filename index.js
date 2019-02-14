var express = require('express'),
	app = express(),
	ejs = require('ejs');

app.set('view engine', 'ejs');


app.get('/', function (req, res){
	res.send('');
});


app.listen(8080, function(){
	console.log('server started on port 3001');
});