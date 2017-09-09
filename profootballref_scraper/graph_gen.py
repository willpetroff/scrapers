import matplotlib.pyplot as plotter
import matplotlib.lines as legend_lines
import csv


qb_age=[]
td_act=[]
td_est=[]
with open('qb_td age_curve.csv','r') as csv_file:
    reader=csv.reader(csv_file)
    for row in reader:
        qb_age.append(row[0])
        td_act.append(row[1])
        td_est.append(row[2])

plotter.plot(qb_age,td_act,qb_age,td_est,'k--')
plotter.ylabel('Toucdowns')
plotter.xlabel('QB Age')
blk_line=legend_lines.Line2D([],[],color='black',marker='',markersize=15,label='Touchdown Estimate')
blue_line=legend_lines.Line2D([],[],color='blue',marker='',markersize=15,label='Touchdown Average')
plotter.legend(handles=[blk_line,blue_line])
plotter.show()
