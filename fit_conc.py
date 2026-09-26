import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import odeint

class ZScanCascadeModel:
    """
    Model for cascade third and fifth-order nonlinearities in chromophore solutions
    Based on Sheik-Bahae formalism with higher-order extensions
    """
    
    def __init__(self):
        self.concentrations = np.array([0.5, 1.0, 2.5, 5.0, 10.0])
        # Your experimental data
        self.delta_phi_3_exp = np.array([3.0, 4.1, 12.6, 9.3, 9.3])
        self.delta_phi_5_exp = np.array([0.8, 0.5, 20.7, 15.4, 15.4])
        self.alpha_3_exp = np.array([0.0, 0.0, 1.8, 2.4, 2.9])
        
    def cascade_phase_model(self, C, n2_0, n4_0, C_sat_3, C_sat_5, alpha_scale):
        """
        Model for concentration-dependent cascade nonlinear phase shifts
        C: concentration array
        n2_0, n4_0: intrinsic nonlinear coefficients
        C_sat_3, C_sat_5: saturation concentrations
        alpha_scale: nonlinear absorption scaling
        """
        # Third-order phase shift with saturation
        delta_phi_3 = n2_0 * C * np.exp(-C / C_sat_3)
        
        # Fifth-order phase shift emerges at higher concentrations
        delta_phi_5 = n4_0 * C**2 * np.exp(-C / C_sat_5)
        
        # Nonlinear absorption develops with concentration
        alpha_3 = alpha_scale * C**3 / (1 + (C / C_sat_5)**2)
        
        return delta_phi_3, delta_phi_5, alpha_3
    
    def fit_experimental_data(self):
        """Fit the cascade model to experimental data"""
        # Initial parameter guesses
        p0 = [15.0, 25.0, 3.0, 4.0, 0.03]
        
        # Fit to delta_phi_3 data
        def fit_func(C, n2_0, n4_0, C_sat_3, C_sat_5, alpha_scale):
            delta_phi_3, _, _ = self.cascade_phase_model(C, n2_0, n4_0, C_sat_3, C_sat_5, alpha_scale)
            return delta_phi_3
        
        popt, pcov = curve_fit(fit_func, self.concentrations, self.delta_phi_3_exp, p0=p0)
        
        return popt
    
    def plot_results(self, params):
        """Plot experimental data and fitted model"""
        C_fit = np.linspace(0.1, 12, 100)
        delta_phi_3_fit, delta_phi_5_fit, alpha_3_fit = self.cascade_phase_model(C_fit, *params)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Phase shifts plot
        ax1.scatter(self.concentrations, self.delta_phi_3_exp, color='blue', label='ΔΦ₃ exp', s=80)
        ax1.scatter(self.concentrations, self.delta_phi_5_exp, color='red', label='ΔΦ₅ exp', s=80)
        ax1.plot(C_fit, delta_phi_3_fit, 'b-', label='ΔΦ₃ model')
        ax1.plot(C_fit, delta_phi_5_fit, 'r-', label='ΔΦ₅ model')
        ax1.set_xlabel('Concentration (v/v %)')
        ax1.set_ylabel('Phase Shift Magnitude')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.set_title('Nonlinear Phase Shifts vs Concentration')
        
        # Nonlinear absorption plot
        ax2.scatter(self.concentrations, self.alpha_3_exp, color='green', label='α₃ exp', s=80)
        ax2.plot(C_fit, alpha_3_fit, 'g-', label='α₃ model')
        ax2.set_xlabel('Concentration (v/v %)')
        ax2.set_ylabel('α₃ (cm³/W²) × 10⁻⁹')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.set_title('Nonlinear Absorption vs Concentration')
        
        plt.tight_layout()
        plt.show()
        
        return fig

# Usage example
if __name__ == "__main__":
    model = ZScanCascadeModel()
    fitted_params = model.fit_experimental_data()
    figure = model.plot_results(fitted_params)
    
    print("Fitted parameters:")
    param_names = ['n2_0', 'n4_0', 'C_sat_3', 'C_sat_5', 'alpha_scale']
    for name, value in zip(param_names, fitted_params):
        print(f"{name}: {value:.4f}")