<script>
    import { matrix } from './data'
    import Square from './Square.svelte'
</script>


<h1>Bonacic Matrix</h1>
<p>Made with SvelteKit</p>
<div class="shell" style="width: 100vw; align-items: center; justify-content: center">
    {#each matrix as row}
        <div style="margin: 0">
            {#each row as item}
                <!-- <Square illuminated={item == 1}/> -->
                    <div style="height: 2vw; width: 2vw; background-color: {item == 1 ? 'orange' : 'gray'}; display: inline-block; margin: 5px"></div>
            {/each}
        </div>
    {/each}
</div>