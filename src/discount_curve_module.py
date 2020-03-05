import numpy as np

class DiscountCurveProvider():

    def __init__(self, tenors, parcurve, extrap_yrs = None):
        self._tenors = tenors
        self._parcurve = parcurve
        self._extrap_yrs = extrap_yrs

    def bootstrap(self):
        tenors = tenors, parcurve = np.asarray(self._tenors), np.asarray(self._parcurve)
        extrap_yrs = self._extrap_yrs

        target_tenors = np.arange(1, tenors[-1] + 1)
        interp_curve = np.interp(target_tenors, tenors, parcurve)

        # generate annual pmt matrix
        annual_pmts = (np.tril(
                    (interp_curve*np.ones((len(interp_curve),len(interp_curve)))).transpose(),0) 
                    + np.eye(len(interp_curve))
            )

        # solve for zcb prices
        zcb = np.linalg.solve(annual_pmts, np.ones(len(interp_curve)))
        
        # extend zcb
        if (extrap_yrs != None):
            ult_tenor = target_tenors[-1]
            total_yrs = ult_tenor + extrap_yrs
            zcb_ext = np.zeros(total_yrs)
            for i in range(total_yrs):
                zcb_ext[i] = zcb[i] if i < ult_tenor else zcb_ext[i-1] * zcb_ext[i-1] / zcb_ext[i-2] 

            zcb = zcb_ext

        return zcb


if __name__ == "__main__":
    print('Discount Curve')