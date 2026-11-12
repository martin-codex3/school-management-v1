<script lang="ts">
    import CreateAccount from "#lib/components/forms/CreateAccount.svelte";
    import NumberIcon from "@iconify-svelte/tabler/number-1";
    import NumberIcon2 from "@iconify-svelte/tabler/number-2";
    import type { PageProps } from "./$types";
    import Login from "#lib/components/forms/Login.svelte";

    let currentTabIndex: number = $state(1);
    const { form }: PageProps = $props();

    const handleChangeIndex = (index: number) => {
        currentTabIndex = index;
    };
</script>

<section class="h-screen flex items-center justify-center px-5 lg:px-0">
    <div
        class="bg-white rounded-4xl w-full border border-primary-border py-5 px-5 max-w-3xl h-[calc(100vh-3rem)] mx-auto"
    >
        <div class="h-full overflow-auto scrollbar-thin px-5 space-y-10 py-5">
            <div class="flex items-center justify-center gap-5">
                <div class="flex flex-col items-center gap-1">
                    <button
                        aria-label="options button"
                        title="Sign In"
                        onclick={() => handleChangeIndex(1)}
                        class={[
                            "flex items-center justify-center p-3 rounded-full border cursor-pointer transition duration-200 hover:outline-1",
                            currentTabIndex === 1
                                ? "bg-primary-main-purple text-black outline-primary-main-purple"
                                : "",
                        ]}
                    >
                        <NumberIcon height="1.5em" class="shrink-0" />
                    </button>
                    <span class="capitalize text-sm font-semibold">Log in</span>
                </div>

                <div class="flex flex-col items-center gap-1">
                    <button
                        aria-label="options button"
                        title="Create account"
                        onclick={() => handleChangeIndex(2)}
                        class={[
                            "flex items-center justify-center p-3 rounded-full border cursor-pointer transition duration-200 hover:outline-1",
                            currentTabIndex === 2
                                ? "bg-primary-main-purple text-black outline-primary-main-purple"
                                : "",
                        ]}
                    >
                        <NumberIcon2 height="1.5em" class="shrink-0" />
                    </button>
                    <span class="capitalize font-semibold text-sm"
                        >create account</span
                    >
                </div>
            </div>

            <div>
                {#if currentTabIndex === 1}
                    <Login {form} />
                {:else if currentTabIndex === 2}
                    <CreateAccount {form} />
                {/if}
            </div>
        </div>
    </div>
</section>
