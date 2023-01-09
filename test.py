from logger import logging

class Test:
    def __init__(self,arg1,arg2):
        self.arg1=arg1
        self.arg2=arg2

    def add(self):
        logging.info("Adding ARG 1 - [{}] ARG2 [{}]".format(self.arg1,self.arg2))


if __name__=="__main__":
    job_id = "123456"
    logging= logging()
    logging.set_log_file(job_id)
    logging.info("******************************")
    logging.info("     TEST CASES               ")
    logging.info("******************************")
    res =  Test(1,2)
    res.add()

