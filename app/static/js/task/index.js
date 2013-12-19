/**
 * Created with PyCharm.
 * User: myth
 * Date: 13-12-6
 * Time: 下午5:13
 * To change this template use File | Settings | File Templates.
 */
(function() {
    $(function() {

        $(document).on("click", ".gridly .brick", function(event) {
            var $this, size;
            event.preventDefault();
            event.stopPropagation();
            $this = $(this);
            $this.toggleClass('small');
            $this.toggleClass('large');
            if ($this.hasClass('small')) {
                size = 140;
            }
            if ($this.hasClass('large')) {
                size = 300;
            }
            $this.data('width', size);
            $this.data('height', size);
            return $('.gridly').gridly('layout');
        });

        $(document).on("click", ".gridly .delete", function(event) {
            var $this;
            event.preventDefault();
            event.stopPropagation();
            $this = $(this);
            $this.closest('.brick').remove();
            return $('.gridly').gridly('layout');
        });

        $(document).on("click", ".add", function(event) {
            var brick = "<div class='brick small' ><div class='delete'>&times;</div></div>";
            event.preventDefault();
            event.stopPropagation();
            $('.gridly').append(brick);
            return $('.gridly').gridly();
        });

        var reordering = function($elements) {
          // Called before the drag and drop starts with the elements in their starting position.

        };

        var reordered = function($elements) {
          // Called after the drag and drop ends with the elements in their ending position.

        };

//        return $('.gridly').gridly({
////            base: 60, // px
////            gutter: 20, // px
////            columns: 12,
////            draggable: { handle: '.move' },
//            callbacks: { reordering: reordering , reordered: reordered }
//        });
    });

}).call(this);
