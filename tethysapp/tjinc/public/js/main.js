require(["esri/map", "dojo/domReady!"], function(Map) {
  var map = new Map("hydromap", {
    center: [-118, 34.5],
    zoom: 8,
    basemap: "topo"
  });
});