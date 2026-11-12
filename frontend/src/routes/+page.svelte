<script lang="ts">
    import NumberIcon from "@iconify-svelte/tabler/number-1";
    import NumberIcon2 from "@iconify-svelte/tabler/number-2";
</script>

<section class="h-screen flex items-center justify-center px-5 lg:px-0">
    <div
        class="bg-white rounded-4xl w-full border border-primary-border py-5 px-5 max-w-3xl h-[calc(100vh-3rem)] mx-auto"
    >
        <div class="h-full overflow-auto scrollbar-thin px-5 space-y-10 py-5">
            <div class="flex items-center justify-center gap-5">
                <button
                    aria-label="options button"
                    title="Sign In"
                    class="flex items-center justify-center p-3 rounded-full border cursor-pointer transition duration-200 hover:outline-1 outline-primary-main-purple text-primary-main-purple"
                >
                    <NumberIcon height="1.5em" class="shrink-0" />
                </button>

                <button
                    aria-label="options button"
                    title="Create account"
                    class="flex items-center justify-center p-3 rounded-full border cursor-pointer transition duration-200 hover:outline-1 outline-primary-main-purple text-primary-main-purple"
                >
                    <NumberIcon2 height="1.5em" class="shrink-0" />
                </button>
            </div>

            <div></div>
        </div>
    </div>
</section>
