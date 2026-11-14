<script lang="ts">
    let { children } = $props();
</script>

<main>
    <nav class="bg-white h-screen max-w-80">
        <!-- for the app logo -->
        <div>
            <h1>main logo</h1>
        </div>

        <!-- for the main links -->
        <div>
            <h1>links</h1>
        </div>

        <!-- for the profile links here -->
        <div>
            <h1>profile</h1>
        </div>
    </nav>

    <section>
        {@render children()}
    </section>
</main>
