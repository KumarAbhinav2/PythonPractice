import multiprocessing as mp
import time
list_of_days = ["2017.03.20", "2017.03.21", "2017.03.22", "2017.03.23", "2017.03.24"]
import pandas as pd
import os

# mp.Queue exeptions have to load from
try:
    # Python3
    import queue
except:
    # Python 2
    import Queue as queue

def f2(fq, q):
    while True:
        try:
            k = fq.get_nowait()
        except queue.Empty:
            exit(0)

        # *** DO SOME STUFF HERE***

        results = pd.DataFrame({'a': range(5), 'b': range(5)}, index=range(5))
        q.put( (list_of_days[k], results) )
        time.sleep(0.1) 


def w(q):
    writer = pd.ExcelWriter('myfile.xlsx', engine='xlsxwriter')
    while True:
        try:
            titel, result = q.get()
        except ValueError:
            writer.save()
            exit(0)

        result.to_excel(writer, sheet_name=titel)


if __name__ == '__main__':
	w_q = mp.Queue()
	w_p = mp.Process(target=w, args=(w_q,))
	w_p.start()
	time.sleep(0.1)	
	f_q = mp.Queue()
	for i in range(5):
		f_q.put(i)

	pool = [mp.Process(target=f2, args = (f_q, w_q)) for p in range(os.cpu_count()+1)]
	for p in pool:
		p.start()
		time.sleep(0.1)

	for p in pool:
		p.join()

	w_q.put('STOP')

	w_p.join()
