import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


class MACDVisualization:

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    IMAGE_PATH = f'MACD_plot_{current_time}.png'

    def visualize(self, data: pd.DataFrame, signal: str) -> None:
        """
        Main visualization method to plot MACD and signal lines based on the input data.
        """
        # Convert column 'C' to numeric type
        data['C'] = pd.to_numeric(data['C'], errors='coerce')

        # Check if data has required columns
        self._check_required_columns(data)

        # Format the dataframe
        data = self._format_dataframe(data)

        # Set up the plot
        fig, axes = self._setup_plot()

        # Plot price and MACD data
        self._plot_price_data(data, axes[0])
        self._plot_macd_data(data, axes[1])

        # Mark buy/sell signals on the plot
        self._mark_signals(data, axes[0], signal)

        # Adjust axes and legend
        for ax in axes:
            self._adjust_axes(data, ax)
            ax.legend(loc='upper right')

        plt.tight_layout()
        plt.savefig(self.IMAGE_PATH, bbox_inches='tight')

    @staticmethod
    def _check_required_columns(data: pd.DataFrame) -> None:
        """
        Ensures the dataframe has the necessary columns for visualization.
        """
        required_columns = {'macd', 'signal', 'C'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"The DataFrame is missing required columns: {', '.join(required_columns)}")

    @staticmethod
    def _format_dataframe(data: pd.DataFrame) -> pd.DataFrame:
        """
        Formats the dataframe for visualization.
        """
        data['T'] = pd.to_datetime(data['T'], unit='ms')
        data.set_index('T', inplace=True)
        return data

    @staticmethod
    def _setup_plot():
        """
        Sets up the main plot for visualization.
        """
        return plt.subplots(nrows=2, ncols=1, figsize=(14, 8), gridspec_kw={'height_ratios': [2.5, 1]})

    @staticmethod
    def _plot_price_data(data: pd.DataFrame, ax) -> None:
        """
        Plots the price data.
        """
        data['C'].plot(ax=ax, color='blue', label='Close Price')
        ax.set_title('Price & MACD Visualization')
        ax.set_ylabel('Price')
        ax.set_xlabel('Time')

    @staticmethod
    def _plot_macd_data(data: pd.DataFrame, ax) -> None:
        """
        Plots the MACD and signal lines.
        """
        data['macd'].plot(ax=ax, color='red', label='MACD')
        data['signal'].plot(ax=ax, color='green', linestyle='dashed', label='Signal Line')
        ax.set_xlabel('Time')

    @staticmethod
    def _mark_signals(data: pd.DataFrame, ax, signal: str) -> None:
        """
        Marks the buy or sell signal on the plot.
        """
        if signal == "buy":
            ax.scatter(data.index[-1], data['C'].iloc[-1], marker='^', color='green', label='Buy Signal', alpha=1,
                       s=100)
            ax.annotate('Buy Signal', (data.index[-1], data['C'].iloc[-1]), textcoords="offset points", xytext=(0, 10),
                        ha='center')
        elif signal == "sell":
            ax.scatter(data.index[-1], data['C'].iloc[-1], marker='v', color='red', label='Sell Signal', alpha=1,
                       s=100)
            ax.annotate('Sell Signal', (data.index[-1], data['C'].iloc[-1]), textcoords="offset points",
                        xytext=(0, -15), ha='center')

    @staticmethod
    def _adjust_axes(data, ax):
        """
        Adjusts the axes for better visualization.
        """
        max_date = data.index[-1]
        min_date = data.index[0]
        date_range = max_date - min_date
        shift_amount = date_range / 3
        ax.set_xlim(min_date, max_date + shift_amount)
