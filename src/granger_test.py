def granger_test(model, causing, caused: str, alpha: float = 0.05):
    """
    Works for:
    - Single variable: 'VIX'
    - Multiple variables: ['VIX', 'BRENT', 'DXY']
    """

    # Ensure causing is always a list for VAR
    if isinstance(causing, str):
        causing_list = [causing]
    else:
        causing_list = causing

    # Detect model type
    if hasattr(model, "test_granger_causality"):
        # VECM (only supports single variable)
        if len(causing_list) > 1:
            raise ValueError("VECM does not support multi-variable causality test")
        
        result = model.test_granger_causality(
            causing=causing_list[0],
            caused=caused
        )
        test_stat = result.test_statistic
        crit_val = result.crit_value
        pval = result.pvalue

    elif hasattr(model, "test_causality"):
        # VAR
        result = model.test_causality(caused, causing_list)
        test_stat = result.test_statistic
        crit_val = result.crit_value
        pval = result.pvalue

    else:
        raise ValueError("Model not supported")

    # Pretty print
    causing_str = ", ".join(causing_list)

    print(f"\nGranger Causality Test: {causing_str} → {caused}")
    print("-" * 60)
    print(f"Null Hypothesis : {causing_str} does NOT Granger-cause {caused}")
    print(f"Test Statistic  : {test_stat:.3f}")
    print(f"Critical Value  : {crit_val:.3f}")
    print(f"P-value         : {pval:.5f}")

    if pval < alpha:
        print(f"Conclusion      : Reject H0 (Significant at {int(alpha*100)}%)")
    else:
        print(f"Conclusion      : Fail to reject H0")

    return 