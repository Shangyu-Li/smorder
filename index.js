var express 	= require('express'),
	ejs 		= require('ejs'),
	path 		= require('path'),
	bodyParser 	= require('body-parser'),
	mysql 		= require('mysql'),
	app 		= express(),
	request		= require('request');


var options		={}

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

// app.use(express.json());
// app.use(express.urlencoded());
//app.use('/',  router);

dirname = path.join(__dirname + '\\CustomerView.html')


app.get('/CustomerView', function (req, res){
	res.sendFile(dirname);
});


app.post('/customer_submit', function (req, res){
	options={
		uri		: 'http://localhost:5000/customer_order',
		body 	: JSON.stringify(req.body),
		method 	: 'POST',
		headers :{
			'Content-Type' : 'text/plain'
		}	
	}
	
	request(options, function(error, response){
		if(error){
			console.log(error)
		}
		return
	})
	res.sendFile(dirname)
});



app.listen(8080, function(){
	console.log('server started on port 8080');
});