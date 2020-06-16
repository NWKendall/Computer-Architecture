"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0
        self.reg = [0] * 8
        self.LDI = 0b10000010
        self.PRN = 0b01000111
        self.HLT = 0b00000001

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000, # address 0
            0b00001000, # store value 8
            0b01000111, # PRN R0 (i.e. print 8)
            0b00000000, # ??
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            # print(instruction)
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU.
        
        1. read mem at PC
        2. store result in local var
        """

        running = True

        while running:
            IR = self.ram[self.pc]
            if IR == self.LDI:
                self.ldi()
            if IR == self.PRN:
                self.prn()           
            if IR == self.HLT:
                running = self.hlt()

    def ram_read(self, address):
        # accept address
        # return it's value
        return self.ram[address]

    def ram_write(self, value, address):
        # take a value
        # write to address
        # no return
        self.ram[address] = value

    def hlt(self):
        self.pc += 1
        return False
    
    def prn(self):
        reg_id = self.ram[self.pc + 1]
        print(self.reg[reg_id])
        self.pc +=2
    
    def ldi(self):
        reg_id = self.ram[self.pc + 1]
        value = self.ram[self.pc + 2]
        self.reg[reg_id] = value
        self.pc += 3
