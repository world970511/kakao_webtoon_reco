var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0],
    offset: 'bottom-in-view',
    onBeforePageLoad: function () {
      $('.loading-data').show();
    },
    onAfterPageLoad: function ($items) {
      $('.loading-data').hide();
    }
  });