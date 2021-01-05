const Toast = (obj, toastVnode = {}) => {
  const h = obj.$createElement;

  const vNodesMsg = h("p", { class: ["text-center", "mb-0"] }, [
    h("nly-spinner", { props: { type: "grow", sm: true } }),
    h("strong", {}, toastVnode.content),
    `#${toastVnode.message}`,
    h("nly-spinner", { props: { type: "grow", sm: true } })
  ]);

  const vNodesTitle = h(
    "div",
    { class: ["d-flex", "flex-grow-1", "align-items-baseline", "mr-2"] },
    [
      h("strong", { class: "mr-2" }, toastVnode.title)
      // h("small", { class: "ml-auto text-italics" }, "刚刚")
    ]
  );

  obj.$nlyaToast.toast([vNodesMsg], {
    title: [vNodesTitle],
    solid: true,
    variant: toastVnode.variant,
    toaster: "nly-toaster-top-center"
  });
};

export default Toast;
