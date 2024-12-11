<script>
    export let illuminated = false
    export let offColor = "gray";
    export let onColor = "orange";
</script>

<div class="square {illuminated ? ' illuminated' : ''}"></div>

<style>
    .square {
        height: 10vw;
        width: 10vw;
        background-color: offColor;
    }

    .illuminated {
        background-color: onColor;
    }

</style>