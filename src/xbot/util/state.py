def default_state():
    state = dict(
        user_action=[],
        system_action=[],
        belief_state={},
        cur_domain=None,
        request_slots=[],
        terminated=False,
        history=[],
    )
    state["belief_state"] = {
        "景点": {
            "名称": "",
            "门票": "",
            "游玩时间": "",
            "评分": "",
            "周边景点": "",
            "周边餐馆": "",
            "周边酒店": "",
        },
        "餐馆": {
            "名称": "",
            "推荐菜": "",
            "人均消费": "",
            "评分": "",
            "周边景点": "",
            "周边餐馆": "",
            "周边酒店": "",
        },
        "酒店": {
            "名称": "",
            "酒店类型": "",
            "酒店设施": "",
            "价格": "",
            "评分": "",
            "周边景点": "",
            "周边餐馆": "",
            "周边酒店": "",
        },
        "地铁": {
            "出发地": "",
            "目的地": "",
        },
        "出租": {
            "出发地": "",
            "目的地": "",
        },
    }
    return state
