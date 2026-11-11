<script lang="ts">
    import TextInput from "#lib/components/inputs/TextInput.svelte";
</script>

<section class="h-screen flex items-center justify-center">
    <div
        class="bg-white rounded-4xl w-full border border-primary-border max-w-2xl h-[calc(100vh-3rem)] mx-auto overflow-hidden"
    >
        <div class="h-full overflow-auto scrollbar-thin">
            <div class="flex items-center justify-center">
                <button
                    aria-label="options button"
                    title="Sign In"
                    class="flex items-center justify-center p-3 rounded-full border"
                ></button>
            </div>
        </div>

        <div>
            <form action="">
                <div
                    class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5"
                >
                    <TextInput></TextInput>
                </div>
            </form>
        </div>
    </div>
</section>
