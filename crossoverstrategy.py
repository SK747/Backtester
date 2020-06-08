import math
import backtrader as bt 

class GCrossover(bt.strategies):
    params = (('fast' , 20), ('slow', 60), ('order_percentage', 0.95),('ticker', 'SPY'))
    
    def __init__(self):
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period = self.params.fast, plotname = '20 day moving average'
        )
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname = '60 day moving average'
        )
        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)
        
    def next (self):
        if self.position.size == 0:
            if self.crossover > 0:
                amount_to_invest = (self.params.order_percentage + self.broker.cash)
                self.size = math.floor (amount_to_invest / self.data.close)
                
                
                self.buy(size = self.size)
                
        if self.position.size > 0:
            if self.crossover < 0:
                self.close()