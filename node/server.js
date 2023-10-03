var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
		myUptime=os.uptime();
		totalMem=Math.round(os.totalmem() / (1024 * 1024));
		freeMem=Math.round(os.freemem() / (1024 * 1024));
		numCPU=os.cpus().length;
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${formatUptime(myUptime)}</p>
            <p>Total Memory: ${totalMem} MB</p>
            <p>Free Memory: ${freeMem} MB</p>
            <p>Number of CPUs: ${numCPU}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");

function formatUptime(uptime) {
	const days = Math.floor(uptime / (60 * 60 * 24));
	const hours = Math.floor((uptime % (60 * 60 * 24)) / (60 * 60));
	const minutes = Math.floor((uptime % (60 * 60)) / 60);
	const seconds = Math.floor(uptime % 60);
	
	return `${days} Days, ${hours} Hours, ${minutes} Minutes, ${seconds} Seconds`;
}
