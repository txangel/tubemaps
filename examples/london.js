var TubeMap = require('../').TubeMap;
var readCSVs = require('../').readCSVs;

var files = {
  connections: __dirname + '/../datasets/london.connections.csv',
  lines: __dirname + '/../datasets/london.lines.csv',
  stations: __dirname + '/../datasets/london.stations.csv'
};

readCSVs(files, function(err, csvs) {

  var tubemap = new TubeMap({
    connections: csvs[0],
    lines: csvs[1],
    stations: csvs[2]
  });

  // How many connections does Victoria station have?
  var victoria = tubemap.getStationByName('Victoria');
  console.log(victoria.conns.length / 2)

});