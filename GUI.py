from Tkinter import *
from Solver import Solver
from State import State
from Euclidean import Euclidean
from DFS import DFS
from BFS import BFS


class GUI:
	
	def __init__(self):
		self.started = False
		self.homePage = False
		self.mainFrame = Tk()
		self.mainFrame.title("8 Puzzle")
		Grid.rowconfigure(self.mainFrame, 0, weight=1)
		Grid.columnconfigure(self.mainFrame, 0, weight=1)
		self.boardFrame = Frame(self.mainFrame,bg = "white") 
		self.board = [[0,1,2],[3,4,5],[6,7,8]]
		self.labels = [[0 for x in range(3)] for y in range(3)]
		for i in range(0,3):
			Grid.rowconfigure(self.boardFrame, i, weight=1)
			for j in range(0,3):
				Grid.columnconfigure(self.boardFrame, j, weight=1)
				if not (i == 0 and j == 0):
					self.labels[i][j] = Button(self.boardFrame,text=str(i*3+j),font=('Times 26 bold'),height = 5 , width = 18,bg='#444488',fg='white')

		
		self.labels[0][1].config(command = lambda:self.move(1))
		self.labels[0][2].config(command = lambda:self.move(2))

		self.labels[1][0].config(command = lambda:self.move(3))
		self.labels[1][1].config(command = lambda:self.move(4))
		self.labels[1][2].config(command = lambda:self.move(5))

		self.labels[2][0].config(command = lambda:self.move(6))
		self.labels[2][1].config(command = lambda:self.move(7))
		self.labels[2][2].config(command = lambda:self.move(8))

		self.BottomFrame = Frame(self.mainFrame,bg = "white")
		self.labelsFrame = Frame(self.BottomFrame,bg = "white")
		self.ButtonsFrame = Frame(self.BottomFrame,bg = "gray")
		Grid.rowconfigure(self.BottomFrame, 0, weight=1)
		Grid.columnconfigure(self.BottomFrame, 0, weight=1)
		
		self.loadingLabel = Label(self.labelsFrame,text='Shuffle it with your self...',bg='white',fg='#888888')
		self.startButton = Button(self.ButtonsFrame,bg='white',fg='#444488',text='Start',font=('Times 18 bold'),command =lambda:self.start())
		
		
		self.backButton = Button(self.ButtonsFrame,bg='white',fg='black',text=' back ',font=('Times 18 bold'),command =lambda:self.backButtonAction())
		self.backButton.config(state=DISABLED)

		
		self.loadingLabel.pack()
		self.startButton.pack(side=RIGHT)		
		
		self.labelsFrame.grid(row=0,column=0,sticky="nsew")
		self.ButtonsFrame.grid(row=1,column=0,sticky="nsew")

		

		




	def start(self):
		self.started = True
		self.homePage = False
		self.startButton.pack_forget()
		self.initialBoard = self.board		
		self.backButton.pack(side=LEFT)
		self.buttons = []
		for i in range(0,4):
			button = Button(self.ButtonsFrame,bg='white',fg='#444488',font=('Times 18 bold'))
			self.buttons.append(button) 
			self.buttons[i].pack(side=LEFT,expand=YES,fill=BOTH)
		initialState = State(self.board,'',None)
		self.buttons[0].config(text=' DFS ',command =lambda: self.solveButtonAction(DFS(initialState)))
		self.buttons[1].config(text=' BFS ',command =lambda: self.solveButtonAction(BFS(initialState)))
		self.buttons[2].config(text='A* (Euclidean)',command =lambda: self.solveButtonAction(Euclidean(initialState)))
		self.buttons[3].config(text='A* (Manhattan)',command =lambda: self.solveButtonAction(Solver(initialState)))
		self.nextButton = Button(self.ButtonsFrame,bg='white',fg='#444488',text=' Next >>',font=('Times 18 bold'),command =lambda:self.nextButtonAction())
		self.previousButton = Button(self.ButtonsFrame,bg='white',fg='#444488',text='<< Previous ',font=('Times 18 bold'),state=DISABLED,command =lambda:self.previousButtonAction())
		self.endButton = Button(self.ButtonsFrame,bg='white',fg='#444488',text=' END ',font=('Times 18 bold'),command =lambda:self.endButtonAction())
		self.beginButton = Button(self.ButtonsFrame,bg='white',fg='#444488',text=' BEGINNING ',font=('Times 18 bold'),command =lambda:self.beginButtonAction())
		self.costLabel = Label(self.labelsFrame,bg='white',fg='#888888')
		self.exploredLabel = Label(self.labelsFrame,bg='white',fg='#888888')
		self.depthLabel = Label(self.labelsFrame,bg='white',fg='#888888')
		self.timeLabel = Label(self.labelsFrame,bg='white',fg='#888888')
		self.stepsLabel = Label(self.labelsFrame,bg='white',fg='#444488')
		self.backButton.config(state="normal")
		self.startHomePage()	

	def startHomePage(self):
		self.homePage = True
		self.nextButton.pack_forget()
		self.previousButton.pack_forget()	
		self.beginButton.pack_forget()
		self.endButton.pack_forget()
		self.costLabel.pack_forget()
		self.exploredLabel.pack_forget()
		self.depthLabel.pack_forget()
		self.timeLabel.pack_forget()
		self.stepsLabel.pack_forget()
		
		self.nextButton.config(state="normal")
		self.previousButton.config(state=DISABLED)	
		self.beginButton.config(state=DISABLED)
		self.endButton.config(state="normal")		

		self.board = self.initialBoard		
		self.currentStep = 0
		self.display()
		for i in range(0,4):
			self.buttons[i].pack(side=LEFT,expand=YES,fill=BOTH)
		self.loadingLabel.config(text = "Choose searching technic")
		self.loadingLabel.pack()


	def startShufflePage(self):
		self.started = False
		self.homePage = False
		self.nextButton.pack_forget()
		self.previousButton.pack_forget()	
		self.beginButton.pack_forget()
		self.endButton.pack_forget()
		self.costLabel.pack_forget()
		self.exploredLabel.pack_forget()
		self.depthLabel.pack_forget()
		self.timeLabel.pack_forget()
		self.stepsLabel.pack_forget()
		for i in range(0,4):
			self.buttons[i].pack_forget()
		self.nextButton.config(state="normal")
		self.previousButton.config(state=DISABLED)	
		self.beginButton.config(state=DISABLED)
		self.endButton.config(state="normal")
		self.board = [[0,1,2],[3,4,5],[6,7,8]]
		self.initialBoard = [[0,1,2],[3,4,5],[6,7,8]]		
		self.currentStep = 0
		self.display()
		self.loadingLabel.config(text = "Shuffle it with your self...")
		self.startButton.pack(side=RIGHT)
		self.backButton.pack_forget()
		self.loadingLabel.pack()
		

	def backButtonAction(self):
		if(self.homePage):
			self.startShufflePage()
		else:
			self.startHomePage()

	def display(self):
		for i in range(0,3):
			for j in range(0,3):
				if (self.board[i][j] != 0):
					x,y = divmod(self.board[i][j],3)
					self.labels[x][y].grid(row=i,column=j,sticky="nsew")

	def position(self,number):
		for i in range(0,3):
			for j in range(0,3):
				if self.board[i][j] == number:
					return [i,j]
		return [0,0]


	def move(self,no):
		if not self.started:
			x,y = map(int,self.position(0))
			i,j = map(int,self.position(no))
			if((i==x-1 and j==y) or (i==x+1 and j==y) or (i==x and j==y-1) or (i==x and j==y+1) ):
				self.board[i][j],self.board[x][y]=self.board[x][y],self.board[i][j]
			self.display()
	

	def solveButtonAction(self,solver):
		self.homePage = False
		self.solver = solver
		self.solver.solve()
		self.solutionPath = self.solver.finalState.getPath()
		self.noOfSteps = len(self.solutionPath)-1
		if self.noOfSteps == 0:
			self.nextButton.config(state=DISABLED)
			self.endButton.config(state=DISABLED)
		self.currentStep = 0

		for i in range(0,4):
			self.buttons[i].pack_forget()
		self.loadingLabel.pack_forget()

		self.costLabel.config(text='cost of the path: {}'.format(solver.finalState.f))
		self.exploredLabel.config(text='    expanded nodes: {}'.format(solver.expandedNodes))
		self.depthLabel.config(text='    search depth: {}'.format(solver.depth))
		self.timeLabel.config(text='     running time: {}'.format(solver.runningTime) + ' seconds')
		self.stepsLabel.config(text='STEP: {}/{}'.format(self.currentStep,self.noOfSteps))
		
		self.costLabel.pack(side=LEFT)
		self.exploredLabel.pack(side=LEFT)
		self.depthLabel.pack(side=LEFT)
		self.timeLabel.pack(side=LEFT)
		self.stepsLabel.pack(side=RIGHT)	

		self.nextButton.pack(side=RIGHT)
		self.previousButton.pack(side=RIGHT)	
		self.beginButton.pack(side=RIGHT)
		self.endButton.pack(side=RIGHT)


	def nextButtonAction(self):
			if self.currentStep < self.noOfSteps:
				self.currentStep += 1
				self.stepsLabel.config(text = 'STEP: {}/{}'.format(self.currentStep,self.noOfSteps))
				if self.currentStep == self.noOfSteps:
					self.nextButton.config(state=DISABLED)
					self.endButton.config(state=DISABLED)
				self.board = self.solutionPath[self.currentStep].board
				self.display()
				if self.currentStep > 0:
					 self.beginButton.config(state="normal")
					 self.previousButton.config(state="normal")
			else:
				self.endButton.config(state=DISABLED)
				self.nextButton.config(state=DISABLED)

	def previousButtonAction(self):
			if self.currentStep > 0:
				self.currentStep -= 1
				self.stepsLabel.config(text = 'STEP: {}/{}'.format(self.currentStep,self.noOfSteps))
				if self.currentStep == 0:
					self.previousButton.config(state=DISABLED)
					self.beginButton.config(state=DISABLED)
				self.board = self.solutionPath[self.currentStep].board
				self.display()
				if self.currentStep < self.noOfSteps:
					 self.endButton.config(state="normal")
					 self.nextButton.config(state="normal")
			else:
				self.previousButton.config(state=DISABLED)
				self.beginButton.config(state=DISABLED)

	def beginButtonAction(self):
			self.currentStep = 0
			self.stepsLabel.config(text = 'STEP: {}/{}'.format(self.currentStep,self.noOfSteps))
			self.board = self.solutionPath[self.currentStep].board
			self.display()
			self.beginButton.config(state=DISABLED)
			self.previousButton.config(state=DISABLED)
			self.endButton.config(state="normal")
			self.nextButton.config(state="normal")

	def endButtonAction(self):
			self.currentStep = self.noOfSteps
			self.stepsLabel.config(text = 'STEP: {}/{}'.format(self.currentStep,self.noOfSteps))
			self.board = self.solutionPath[self.currentStep].board
			self.display()
			self.endButton.config(state=DISABLED)
			self.nextButton.config(state=DISABLED)
			self.beginButton.config(state="normal")
			self.previousButton.config(state="normal")

	def run(self):
		self.display()
		self.boardFrame.grid(row=0,column=0,sticky="nsew")
		self.BottomFrame.grid(row=1,column=0,sticky="nsew")
		self.mainFrame.mainloop()
