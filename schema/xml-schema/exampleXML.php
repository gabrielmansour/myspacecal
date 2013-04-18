<?php
     if(isset($_GET["start"]) && isset($_GET["end"]))
     {
        echo '<?xml version="1.0" encoding="UTF-8"?>';
        echo '<events>';
        echo '<event>';
        echo '<observationId>0</observationId>';
        echo '<startTime>2009-12-16T00:00:00Z</startTime>';
        echo '<endTime>2009-12-16T15:00:00Z</endTime>';
        echo '<target>Vicente</target>';
        echo '<revolution>0</revolution>';
        echo '<ra>1.1</ra>';
        echo '<dec>-1.1</dec>';
        echo '</event>';
        echo '<event>';
        echo '<observationId>1</observationId>';
        echo '<startTime>2009-12-16T18:00:00Z</startTime>';
        echo '<endTime>2009-12-16T19:00:00Z</endTime>';
        echo '<target>Vicente2</target>';
        echo '<revolution>0</revolution>';
        echo '<ra>1.3</ra>';
        echo '<dec>-1.4</dec>';
        echo '</event>';
        echo '</events>';
    }
    else
    {
        echo '<satellite>';
        echo '<actual>0</actual>';
        echo '<maxFuture>0</maxFuture>';
        echo '</satellite>';
     }
?>