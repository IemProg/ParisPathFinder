import setup

class ShowMePath():
    def __init__(self, origin, destination):
        self.graph = setup.Graph()
        self.start = origin
        self.end = destination

    def ShowPath(self):
        return setup.shortest_path(self.graph, self.start, self.end)

    def toString(self):
        if self.start == self.end:
            return "You are in the same location!"
        S = "Best way to get from " + self.start + "to " + self.end + "is: \n"

        Time = self.ShowPath()[0]
        Path = self.ShowPath()[1]

        same_line_flag = True
        Time_temp = 0

        for i in range(len(Path)-2):
            Current = setup.dic_stations[Path[i]]
            Next = setup.dic_stations[Path[i+1]]

            Time_Current = setup.dic_stations[Path[i]].getTime()
            Time_next = setup.dic_stations[Path[i+1]].getTime()

            if Time_Current != Time_next:
                if (Current.getLineID() != Next.getLineID() and Next.getName() != Current.getName()):
                    if (i != 0):
                        S += " to " + Next.name + "(" + Time_temp + " Secs\n"
                        Time_temp = 0
                    S += "Walk to " + Next.getName() + ", Line "+ Next.getLineID + str(Time_next-Time_Current) + "Sec"
                    same_line_flag = True

                if (Current.getLineID() == Next.getLineID() and Current.getName() != Next.getName()):
                    #TODO
                    Time_temp += setup.dict_connections[Path[i].getName()][Path[i+1].getName()]

                if (Current.getName() != Next.getName() and same_line_flag):
                    S += " take line " + Next.getLineID + " "+Next.getLineName() +" \n"
                    S += " from "+ Current.getName()
                    same_line_flag = False

            if (Current.getName() == setup.dic_stations[self.end].getName() or Next.getName() == setup.dic_stations[self.end].getName()):
                i = len(Path) - 1
                S += " to " + Next.getName() + " ("+ Time_temp + " Secs\n"
        S += "You have reached your destination in : "+ Time + "Secs"

        return S

if __name__ == '__main__':
    start, end = input("Where you would like to go ? "
                   "(Start_id End_id) or (Starting station Ending Station ").split()
    print("Start: ", start, "Type: ", type(start))
    print("End: ", end, "Type: ", type(end))

    ShowMePath1 = ShowMePath(start, end)
    #print(ShowMePath1.ShowPath())
    print("\n---------------------------------------------------------------\n")
    print(ShowMePath1.toString())
