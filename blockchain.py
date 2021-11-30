import random
import sys
import base64

import json

from web3 import Web3
from solcx import compile_standard



# struct File {
                        #     string owner;  
                        #     string fid;
                        #     string[] allowed;  

                        # }
                        # File[] files;

# Solidity source code
# uint len = allowed[id].length

#  function getStore() public view returns(string memory){
                        #     return store;
                        #  }
                        #  function setStore(string memory _value) public{
                        #     store=_value;
                        #  }
                        #  function addfile(string memory id) public{
                        #      file[id]=msg.sender;
                        #      allowed[id].push(msg.sender);  
                        #  }
                        #  function getFile(string memory id) public view returns(address[] memory){
                        #      return allowed[id];
                            
                        #  }
                        #  function allow(string memory id, address adr) public{
                        #     allowed[id].push(adr);  
                        #  }
compiled_sol = compile_standard({
     "language": "Solidity",
     "sources": {
         "phb.sol": {
             "content": '''
                 pragma solidity >=0.4.0 <0.6.0;
               

                contract PHB {
                        string store="";
                        mapping(string => address) manufacturer;
                        mapping(string => address) seller;
                        mapping(string => address) customer;
                        mapping(string => string[]) assign;
                        mapping(string => string[]) purchase;
                       

                        

                        constructor() public {
                             store="abcde";
                            
                         }
                        
                         function assign1(string memory id1,string memory id2) public{
                             assign[id1].push(id2); 
                         }
                         function purchase1(string memory id1,string memory id2) public{
                            purchase[id1].push(id2); 
                         }
                       
                    }

               '''
         }
     },
     "settings":
         {
             "outputSelection": {
                 "*": {
                     "*": [
                         "metadata", "evm.bytecode"
                         , "evm.bytecode.sourceMap"
                     ]
                 }
             }
         }
 })


# web3.py instance







def create_contract():
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    # get bytecode
    bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']	['metadata'])['output']['abi']

    pb = w3.eth.contract(abi=abi, bytecode=bytecode)

    # # Submit the transaction that deploys the contract
    tx_hash = pb.constructor().transact()

    # # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print("tx_receipt.contractAddress: ",tx_receipt.contractAddress)
    f=open('contract_address.txt','w')
    f.write(tx_receipt.contractAddress)
    f.close()


def add_customer(val):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = '0x3529A6ee990639C32bEe5F841a9649cdd0c6e0FD'
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    # pb = w3.eth.contract(abi=abi, bytecode=bytecode)

    # # Submit the transaction that deploys the contract
    # tx_hash = pb.constructor().transact()

    # # Wait for the transaction to be mined, and get the transaction receipt
    # tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    #print("tx_receipt.contractAddress: ",tx_receipt.contractAddress)
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )



    tx_hash = p1.functions.setStore(str(val)).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

    tx_hash = p1.functions.addfile(str(val)).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

    # tx_hash = p1.functions.getStore().transact()
    # tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

    store = p1.functions.getStore().call()
    
    # tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

    

    #print(tx_hash)
    print(store)

def get_contract(adr):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = '0x3529A6ee990639C32bEe5F841a9649cdd0c6e0FD'
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    return p1


def assign(id1,id2):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = '0xE92603F8EE605EDe093B900fa1EA8421969adBBA'
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    tx_hash = p1.functions.assign1(str(id1),str(id2)).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_receipt)
    
# def get_assigned(id):
#     p1=get_contract(5)
#     allowed = p1.functions.get_assigned(str(id)).call()
#     print(allowed)

def verify_adr(s):
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected(),"##########")
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    adrs = w3.eth.accounts
    print(adrs)

    if s in adrs:
        return True
    else:
        return False    

def bpayment(adr1,adr2,key,amount):
    try:
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        web3.eth.enable_unaudited_features()
        nonce = web3.eth.getTransactionCount(adr1)

        tx = {
            'nonce': nonce,
            'to': adr2,
            'value': web3.toWei(1, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei(amount, 'gwei'),
        }
        signed_tx = web3.eth.account.signTransaction(tx,key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(web3.toHex(tx_hash))
        return web3.toHex(tx_hash)
    except Exception as e:
        print(e)  
        return False  

def purchase(id1,id2):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = '0xE92603F8EE605EDe093B900fa1EA8421969adBBA'
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    tx_hash = p1.functions.purchase1(str(id1),str(id2)).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_receipt)


def bverify_transaction(tx):
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected(),"##########")
    #w3 = Web3(Web3.EthereumTesterProvi
    x=w3.eth.getTransaction(tx)
    print(x)
    if x==None:
        print('Fake')
        return False
    else:
        print('Real')
        return True



if __name__=="__main__":
    #save_to_block(5)
    #create_contract()
    #allow(5,'0x3529A6ee990639C32bEe5F841a9649cdd0c6e0FD')
    #get_allowed(5)
    #print(verify_adr('0xED8E36D67cD35E2F863E2f7EF90570bb543e60a0'))
    #assign(1,2)
    verify_transaction('0xc54ff78d3e21b45e072351a02bcc4758659d0497e3f9b34dfd7faeb1cd4be073')
    
    #payment('0xB8b84d25a3eaEf0d231D9E422DdE7B21839E6793','0x44b2c1e452B5AA05235cB040773111DE30d53B0f','82a2f61beebb41befafb032060ad6108ba3178c240fdcace93325bca1b6db992','300')