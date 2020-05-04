pragma solidity ^0.5.0;

import "@openzeppelin/contracts/access/Roles.sol";

contract Imune02 {
    using Roles for Roles.Role;

    // criar os roles
    Roles.Role private _admins;
    Roles.Role private _heathfacilities;

    struct BatchStruct {
        address batchAddress;
        address supplier;
        address batchOrigin;
        address responsible;
        string geolocation;
        string documentNumber;
        string document;
        uint256 timestamp;
        uint index;
    }

    struct TransactionBatchStruct {
        address transactionBatchAddress;
        address batchAddress;
        address responsible;
        string geolocation;
        uint256 timestamp;
        uint index;
    }

    struct VaccinateStruct {
        address vaccinateAddress;
        address responsible;
        address batchAddress;
        string documentNumber;
        string document; // cpf, rg, sus, passaport
        uint256 timestamp;
        string vaccine;
        uint index;
    }

    struct OccurrenceStruct {
        address occurrenceAddress;
        address responsible;
        address batchAddress;
        string documentNumber;
        string document; // cpf, rg, sus, passaport
        uint256 timestamp;
        string vaccine;
        string detail;
        uint index;
    }

    mapping(address => BatchStruct) private batchStructs;
    address[] private batchIndex;

    mapping(address => TransactionBatchStruct) private transactionBatchStructs;
    address[] private transactionBatchIndex;

    mapping(address => VaccinateStruct) private vaccinateStructs;
    address[] private vaccinateIndex;

    mapping(address => OccurrenceStruct) private occurrenceStructs;
    address[] private occurrenceIndex;

    constructor(address[] memory admins, address[] memory heathfacilities)
        public {
            // atribui os roles no construtor do contrato
            for (uint256 i = 0; i < admins.length; ++i) {
                _admins.add(admins[i]);
            }

            for (uint256 i = 0; i < heathfacilities.length; ++i) {
                _heathfacilities.add(heathfacilities[i]);
            }
        }

        // adiciona endereco na lista de admin, sendo admin
        function add_admins(address to) public {
            require(_admins.has(msg.sender), "DOES_NOT_HAVE_ADMIN_ROLE");

            _admins.add(to);
        }

        function remove_admins(address to) public {
            require(_admins.has(msg.sender), "DOES_NOT_HAVE_ADMIN_ROLE");

            _admins.remove(to);
        }

        // adiciona endereco na lista de health facilities
        function add_healthfacilities(address to) public {
            require(_admins.has(msg.sender), "DOES_NOT_HAVE_ADMIN_ROLE");

            _heathfacilities.add(to);
        }

        // remover endereco da lista de health facilities
        function remove_healthfacilities(address to) public {
            require(_admins.has(msg.sender), "DOES_NOT_HAVE_ADMIN_ROLE");

            _heathfacilities.remove(to);
        }

        // verifica se um lote existe
        function isBatch(address batchAddress) public view returns(bool isIndeed) {
            if(batchIndex.length == 0) return false;
            return (batchIndex[batchStructs[batchAddress].index] == batchAddress);
        }

        // verifica se uma transacao de lote existe
        function isTransactionBatch(address transactionBatchAddress) public view returns(bool isIndeed) {
            if(transactionBatchIndex.length == 0) return false;
            return (transactionBatchIndex[transactionBatchStructs[transactionBatchAddress].index] == transactionBatchAddress);
        }

        // verifica se uma aplicacao de vacina existe
        function isVaccinate(address vaccinateAddress) public view returns(bool isIndeed) {
            if(vaccinateIndex.length == 0) return false;
            return (vaccinateIndex[vaccinateStructs[vaccinateAddress].index] == vaccinateAddress);
        }

        // verifica se uma ocorrencia
        function isOccurrence(address occurrenceAddress) public view returns(bool isIndeed) {
            if(occurrenceIndex.length == 0) return false;
            return (occurrenceIndex[occurrenceStructs[occurrenceAddress].index] == occurrenceAddress);
        }

        // conta o total de lotes
        function getBatchCount() public view returns(uint count) {
            return batchIndex.length;
        }

        // conta o total de transacoes de lote
        function getTransactionBatchCount() public view returns(uint count) {
            return transactionBatchIndex.length;
        }

        // conta o total de aplicacoes
        function getVaccinateCount() public view returns(uint count) {
            return vaccinateIndex.length;
        }

        // conta o total de ocorrencias
        function getOccurrenceCount() public view returns(uint count) {
            return occurrenceIndex.length;
        }

        // insere um lote
        function insertBatch(
            address batchAddress,
            address supplier,
            address batchOrigin,
            string memory geolocation,
            string memory documentNumber,
            string memory document)
            public
            returns(uint index)
            {
                require(_heathfacilities.has(msg.sender), "DOES_NOT_HAVE_HEALTH_FACILITY_ROLE");

                if(isBatch(batchAddress)) revert();
                batchStructs[batchAddress].supplier = supplier;
                batchStructs[batchAddress].batchOrigin = batchOrigin;
                batchStructs[batchAddress].geolocation = geolocation;
                batchStructs[batchAddress].responsible = msg.sender;
                batchStructs[batchAddress].documentNumber = documentNumber;
                batchStructs[batchAddress].document = document;
                batchStructs[batchAddress].timestamp = now;

                batchStructs[batchAddress].index = batchIndex.push(batchAddress)-1;
                return batchIndex.length-1;
            }

        function getBatch(address batchAddress) public view
            returns(address supplier, address batchOrigin, address responsible,
                string memory geolocation, string memory document, string memory documentNumber, uint index)
            {
                if(!isBatch(batchAddress)) revert();
                return(
                    batchStructs[batchAddress].supplier,
                    batchStructs[batchAddress].batchOrigin,
                    batchStructs[batchAddress].responsible,
                    batchStructs[batchAddress].geolocation,
                    batchStructs[batchAddress].document,
                    batchStructs[batchAddress].documentNumber,
                    batchStructs[batchAddress].index);
            }

        // insere uma transacao de lote
        function insertTransactionBatch(
            address transactionBatchAddress,
            address batchAddress)
            public
            returns(uint index)
            {
                if(isTransactionBatch(transactionBatchAddress)) revert();
                transactionBatchStructs[transactionBatchAddress].batchAddress = batchAddress;
                transactionBatchStructs[transactionBatchAddress].responsible = msg.sender;
                transactionBatchStructs[transactionBatchAddress].timestamp = now;

                transactionBatchStructs[transactionBatchAddress].index = transactionBatchIndex.push(transactionBatchAddress)-1;
                return transactionBatchIndex.length-1;
            }

        // insere uma aplicacao de vacina
        function insertVaccinate(
            address vaccinateAddress,
            address batchAddress,
            string memory documentNumber,
            string memory document,
            string memory vaccine)
            public
            returns(uint index)
            {
                if(isVaccinate(vaccinateAddress)) revert();
                vaccinateStructs[vaccinateAddress].batchAddress = batchAddress;
                vaccinateStructs[vaccinateAddress].responsible = msg.sender;
                vaccinateStructs[vaccinateAddress].documentNumber = documentNumber;
                vaccinateStructs[vaccinateAddress].document = document;
                vaccinateStructs[vaccinateAddress].vaccine = vaccine;
                vaccinateStructs[vaccinateAddress].timestamp = now;

                vaccinateStructs[vaccinateAddress].index = vaccinateIndex.push(vaccinateAddress)-1;
                return vaccinateIndex.length-1;
            }

        function getVaccinate(address vaccinateAddress) public view
            returns(address responsible, address batchAddress, string memory document, string memory documentNumber,
                uint256 timestamp, string memory vaccine, uint index)
            {
                if(!isVaccinate(vaccinateAddress)) revert();
                return(
                    vaccinateStructs[vaccinateAddress].responsible,
                    vaccinateStructs[vaccinateAddress].batchAddress,
                    vaccinateStructs[vaccinateAddress].document,
                    vaccinateStructs[vaccinateAddress].documentNumber,
                    vaccinateStructs[vaccinateAddress].timestamp,
                    vaccinateStructs[vaccinateAddress].vaccine,
                    vaccinateStructs[vaccinateAddress].index);
            }

    // insere uma ocorrencia
    function insertOccurrence(
            address occurrenceAddress,
            address batchAddress,
            string memory documentNumber,
            string memory document,
            string memory vaccine)
            public
            returns(uint index)
            {
                if(isOccurrence(occurrenceAddress)) revert();
                occurrenceStructs[occurrenceAddress].occurrenceAddress = occurrenceAddress;
                occurrenceStructs[occurrenceAddress].batchAddress = batchAddress;
                occurrenceStructs[occurrenceAddress].responsible = msg.sender;
                occurrenceStructs[occurrenceAddress].documentNumber = documentNumber;
                occurrenceStructs[occurrenceAddress].document = document;
                occurrenceStructs[occurrenceAddress].vaccine = vaccine;

                occurrenceStructs[occurrenceAddress].index = occurrenceIndex.push(occurrenceAddress)-1;
                return occurrenceIndex.length-1;
            }

    function getOccurrence(address occurrenceAddress) public view
            returns(address responsible, address batchAddress, string memory document, string memory documentNumber,
                uint256 timestamp, string memory vaccine, uint index)
            {
                if(!isOccurrence(occurrenceAddress)) revert();
                return(
                    occurrenceStructs[occurrenceAddress].responsible,
                    occurrenceStructs[occurrenceAddress].batchAddress,
                    occurrenceStructs[occurrenceAddress].document,
                    occurrenceStructs[occurrenceAddress].documentNumber,
                    occurrenceStructs[occurrenceAddress].timestamp,
                    occurrenceStructs[occurrenceAddress].vaccine,
                    occurrenceStructs[occurrenceAddress].index);
            }
}
